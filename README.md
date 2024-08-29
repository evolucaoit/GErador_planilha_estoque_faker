# 📊 GErador_planilha_estoque_faker

**Autor**: [Elias Andrade](https://github.com/chaos4455e) | [LinkedIn](https://br.linkedin.com/in/itilmgf)

---

## 📝 Visão Geral do Projeto

O **GErador_planilha_estoque_faker** é um projeto desenvolvido para gerar dados fictícios de estoque de maneira eficiente e prática utilizando Python. Este repositório faz parte do meu portfólio e reflete minha expertise em automação, manipulação de dados e geração de dados sintéticos para diversas aplicações empresariais. Através deste projeto, demonstro como habilidades avançadas em programação e manipulação de dados podem ser aplicadas para criar soluções práticas e eficazes.

---

## 🚀 Funcionalidades

- **Geração de Planilhas de Estoque**: Criação de arquivos Excel com dados de estoque fictícios, ideal para testes e simulações.
- **Dois Modos de Geração**:
  - **Básico**: Geração de dados para duas filiais, com detalhes como produto, categoria, quantidade, preço unitário e data de validade. 
  - **Avançado**: Geração de dados para 22 filiais, incluindo ID único, descrição, categoria, quantidade, preço unitário, data de validade e nome da filial.

### 🔗 Exemplos de Planilhas Geradas

- [estoque_transportadora.xlsx](https://github.com/evolucaoit/GErador_planilha_estoque_faker/blob/main/estoque_transportadora.xlsx)
- [estoque_empresas.xlsx](https://github.com/evolucaoit/GErador_planilha_estoque_faker/blob/main/estoque_empresas.xlsx)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

### 🌐 Linguagens e Ferramentas
- **Python**: Linguagem principal utilizada para o desenvolvimento dos scripts.
- **Pandas**: Biblioteca essencial para manipulação e análise de dados, permitindo fácil integração e exportação para formatos como Excel.
- **Faker**: Biblioteca poderosa para a geração de dados fictícios realistas, essencial para simulação e testes.
- **Openpyxl**: Utilizada para manipulação de arquivos Excel diretamente através do Python.

---

## 📊 Diagrama de Conhecimentos e Técnicas

```mermaid
graph TD;
    A[Conhecimentos Necessários] --> B[Python]
    A --> C[Pandas]
    A --> D[Faker]
    A --> E[Openpyxl]
    B --> F[Fundamentos de Programação]
    B --> G[Manipulação de Arquivos]
    C --> H[DataFrames]
    C --> I[Exportação para Excel]
    D --> J[Geração de Dados Fictícios]
    D --> K[Simulações Realistas]
    E --> L[Manipulação de Excel]
    E --> M[Automação de Tarefas]

    subgraph Desenvolvimento dos Scripts
        N[geraplanilhaestoque.py]
        O[geraplanilhaestoqueavancada.py]
    end

    N --> P[Função para gerar dados]
    N --> Q[Criar DataFrame]
    N --> R[Exportar para Excel]
    O --> S[Função Avançada para gerar dados]
    O --> T[Criação de múltiplos DataFrames]
    O --> U[Exportação avançada para Excel]

