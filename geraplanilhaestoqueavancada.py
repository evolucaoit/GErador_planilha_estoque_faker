import pandas as pd
from faker import Faker
import random

# Inicializar o Faker
fake = Faker()

# Função para gerar dados fictícios de estoque
def generate_stock_data(num_records, filial_name):
    data = []
    for _ in range(num_records):
        record = {
            'ID': fake.uuid4(),
            'Descrição': fake.word(),
            'Categoria': random.choice(['Peças', 'Ferramentas', 'Equipamentos', 'Acessórios']),
            'Quantidade': random.randint(1, 500),
            'Preço Unitário': round(random.uniform(10.0, 2000.0), 2),
            'Data de Validade': fake.date_between(start_date='today', end_date='+5y'),
            'Filial': filial_name
        }
        data.append(record)
    return data

# Gerar dados para 22 filiais
num_records = 100  # Número de registros por filial
branches = [f'Filial {i}' for i in range(1, 23)]  # 22 filiais
all_data = []

for branch in branches:
    branch_data = generate_stock_data(num_records, branch)
    all_data.append(pd.DataFrame(branch_data))

# Criar um Excel Writer
with pd.ExcelWriter('estoque_transportadora.xlsx', engine='openpyxl') as writer:
    for df, branch in zip(all_data, branches):
        df.to_excel(writer, sheet_name=branch, index=False)

print("Planilha de estoque gerada com sucesso: estoque_transportadora.xlsx")
