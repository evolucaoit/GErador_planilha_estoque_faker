# 📊 Gerador_planilha_estoque_faker

**Autor**: [Elias Andrade](https://github.com/chaos4455e) | [LinkedIn](https://br.linkedin.com/in/itilmgf)

---
## 📝 Sobre o Autor e o Propósito do Projeto

Este projeto é uma **demonstração do meu domínio e expertise** em **Python** e **manipulação de dados**. Sou Elias Andrade, um profissional apaixonado por tecnologia e inovação, com mais de 14 anos de experiência em infraestrutura de TI e automação. 🚀

### 🎯 Propósito do Projeto

O **GErador_planilha_estoque_faker** foi criado para **mostrar minha habilidade em aplicar linguagens de programação para resolver problemas complexos** e multifacetados. 💡

- **🛠️ Solução Técnica**: Utilizando bibliotecas avançadas como `pandas`, `Faker` e `openpyxl`, este projeto ilustra minha capacidade de gerar dados fictícios realistas e manipulá-los eficientemente para criar planilhas de estoque complexas e úteis.
- **💼 Aplicação Real**: As planilhas geradas são ideais para cenários de teste, simulação e análise de performance, refletindo minha habilidade em desenvolver soluções que podem ser aplicadas em ambientes empresariais reais.
- **🔍 Problemas Multi-facetados**: Este projeto exemplifica minha abordagem para enfrentar desafios diversos, desde a geração de dados até a exportação para formatos complexos, sempre buscando otimizar e automatizar processos.

Para ver mais do meu trabalho e entender como aplico conhecimento técnico em soluções práticas, confira [meu portfólio no GitHub](https://github.com/chaos4455e) e conecte-se comigo no [LinkedIn](https://br.linkedin.com/in/itilmgf). 🌟

---

Este micro projeto reflete a minha jornada e dedicação em criar soluções inovadoras e eficazes, mostrando a aplicação prática de habilidades técnicas em contextos desafiadores. 👨‍💻


## 🌟 Visão Geral do Projeto

O **Gerador_planilha_estoque_faker** é um projeto desenvolvido para gerar dados fictícios de estoque de maneira eficiente e prática utilizando Python 🐍. Este repositório faz parte do meu portfólio 🎒 e reflete minha expertise em automação ⚙️, manipulação de dados 📊 e geração de dados sintéticos para diversas aplicações empresariais 🏢. Através deste projeto, demonstro como habilidades avançadas em programação e manipulação de dados podem ser aplicadas para criar soluções práticas e eficazes 🧠.

---

## 🚀 Funcionalidades

- **📋 Geração de Planilhas de Estoque**: Criação de arquivos Excel 📈 com dados de estoque fictícios, ideal para testes e simulações.
- **⚙️ Dois Modos de Geração**:
  - **🔹 Básico**: Geração de dados para duas filiais 🏬🏬, com detalhes como produto 🛍️, categoria 📂, quantidade 📦, preço unitário 💵 e data de validade 📅.
  - **🔸 Avançado**: Geração de dados para 22 filiais 🏭, incluindo ID único 🔑, descrição 📝, categoria 🗂️, quantidade 📦, preço unitário 💰, data de validade 📅 e nome da filial 🏢.

### 🔗 Exemplos de Planilhas Geradas

- [📂 estoque_transportadora.xlsx](https://github.com/evolucaoit/GErador_planilha_estoque_faker/blob/main/estoque_transportadora.xlsx)
- [📂 estoque_empresas.xlsx](https://github.com/evolucaoit/GErador_planilha_estoque_faker/blob/main/estoque_empresas.xlsx)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

### 🌐 Linguagens e Ferramentas
- **Python** 🐍: Linguagem principal utilizada para o desenvolvimento dos scripts.
- **Pandas** 🐼: Biblioteca essencial para manipulação e análise de dados, permitindo fácil integração e exportação para formatos como Excel.
- **Faker** 🎭: Biblioteca poderosa para a geração de dados fictícios realistas, essencial para simulação e testes.
- **Openpyxl** 📘: Utilizada para manipulação de arquivos Excel diretamente através do Python.

---

## 📊 Diagrama de Conhecimentos e Técnicas

### Conhecimentos Necessários
- **Python** 🐍
  - Fundamentos de Programação 🧩
  - Manipulação de Arquivos 📝
- **Pandas** 🐼
  - DataFrames 📊
  - Exportação para Excel 📤
- **Faker** 🎭
  - Geração de Dados Fictícios 🎲
  - Simulações Realistas 🧪
- **Openpyxl** 📘
  - Manipulação de Excel 📑
  - Automação de Tarefas 🤖

### Desenvolvimento dos Scripts
- **geraplanilhaestoque.py** 📄
  - Função para gerar dados 🧠
  - Criar DataFrame 🖥️
  - Exportar para Excel 📂
- **geraplanilhaestoqueavancada.py** 📄
  - Função Avançada para gerar dados 🚀
  - Criação de múltiplos DataFrames 📋
  - Exportação avançada para Excel 📤

---

## 🎯 Aplicações Práticas em Projetos Reais

- **🛠️ Teste de Sistemas**: Ideal para criar cenários de teste em sistemas ERP 🖥️, garantindo que diferentes módulos funcionem corretamente com uma variedade de dados de entrada.
- **📈 Machine Learning**: Perfeito para gerar datasets que podem ser usados no treinamento de modelos preditivos, como previsão de demanda 🔍 e otimização de estoque 📦.
- **⚡ Análise de Performance**: Útil para simular cenários e avaliar o desempenho de sistemas de gerenciamento de estoque sob diferentes condições 📊.
- **🎓 Demonstrações e Treinamentos**: Ótimo para criar material de treinamento para equipes 👥 ou para demonstrar a capacidade de ferramentas de análise de dados 🛠️.

---

## 🧠 Estrutura dos Scripts e Lógica Implementada

### **📄 geraplanilhaestoque.py**

1. **🔍 Inicialização do Faker**: Utiliza o `Faker` para criar dados fictícios de estoque, como nome do produto, categoria, quantidade e preço.
2. **🛠️ Geração de Dados**: Função `generate_stock_data` cria uma lista de dicionários com os dados gerados.
3. **📊 Criação de DataFrames**: Utiliza `pandas` para organizar os dados em DataFrames, representando cada filial.
4. **📤 Exportação para Excel**: Utiliza `openpyxl` para salvar os dados em um arquivo Excel com múltiplas planilhas.

### **📄 geraplanilhaestoqueavancada.py**

1. **🚀 Geração de Dados Avançada**: Similar ao script básico, mas com adição de campos como ID único e múltiplas categorias de produtos.
2. **🏢 Geração para Múltiplas Filiais**: Função `generate_stock_data` adaptada para incluir o nome da filial, permitindo a criação de planilhas separadas para até 22 filiais.
3. **⚙️ Automação de Exportação**: Script otimizado para exportar todas as planilhas em um único arquivo Excel.

---

Obrigado por visitar o repositório! 🚀 Para mais projetos e atualizações, acompanhe meu trabalho no [GitHub](https://github.com/chaos4455) e conecte-se comigo no [LinkedIn](https://br.linkedin.com/in/itilmgf). 😃

