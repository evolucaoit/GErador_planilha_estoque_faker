import pandas as pd
from faker import Faker
import random

# Inicializar o Faker
fake = Faker()

# Função para gerar dados fictícios de estoque
def generate_stock_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'Produto': fake.word(),
            'Categoria': fake.word(),
            'Quantidade': random.randint(1, 100),
            'Preço Unitário': round(random.uniform(5.0, 100.0), 2),
            'Data de Validade': fake.date_between(start_date='today', end_date='+2y')
        }
        data.append(record)
    return data

# Gerar dados para duas filiais
num_records = 50
branch1_data = generate_stock_data(num_records)
branch2_data = generate_stock_data(num_records)

# Criar DataFrames
df_branch1 = pd.DataFrame(branch1_data)
df_branch2 = pd.DataFrame(branch2_data)

# Criar um Excel Writer
with pd.ExcelWriter('estoque_empresas.xlsx', engine='openpyxl') as writer:
    df_branch1.to_excel(writer, sheet_name='Filial 1', index=False)
    df_branch2.to_excel(writer, sheet_name='Filial 2', index=False)

print("Planilha de estoque gerada com sucesso: estoque_empresas.xlsx")
