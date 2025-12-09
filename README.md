# 📦 Previsão do Tempo de Entrega de Pedidos (Brazilian E‑Commerce — Olist)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Orange](https://img.shields.io/badge/Orange-Data%20Mining-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este projeto de **Machine Learning** tem como objetivo prever o **tempo exato de entrega (em dias)** de pedidos de e-commerce, utilizando dados reais da plataforma Olist. A solução combina processamento de dados em **Python** com modelagem visual no **Orange Data Mining**.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Resultados e Métricas](#-resultados-e-métricas)
- [Como Executar](#-como-executar)
- [Autor](#-autor)

## 🧐 Visão Geral

A logística é um componente crítico no e-commerce. A capacidade de estimar com precisão quando um cliente receberá seu produto impacta diretamente a satisfação e a fidelização.

Neste projeto, utilizamos o **[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** para treinar modelos de regressão. O fluxo de trabalho consiste em:
1.  **Engenharia de Atributos (Python):** Limpeza, agregação de itens e criação de variáveis temporais (ex: dia da semana da compra, diferença entre data estimada e real).
2.  **Modelagem (Orange):** Comparação de algoritmos como Random Forest, kNN, SVM e Regressão Linear.

## Estrutura do repositório

```bash
olist-delivery-time-lm/
├── data/
│   ├── processed/          # Dados processados prontos para o Orange (orders_features.csv)
│   └── raw/                # Dados brutos originais do Olist (csv)
├── orange_workflow/
│   └── olist_workflow.ows  # Fluxo de modelagem do Orange Data Mining
├── results/
│   ├── metrics.csv         # Tabela comparativa de performance dos modelos
│   └── best_model_prediction_sample.csv
├── prepare_data.py         # Script Python para pré-processamento e ETL
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── LICENSE                 # Licença MIT
```

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: [Python](https://www.python.org/)

- **Bibliotecas**: [Pandas](https://pandas.pydata.org/) (manipulação de dados).

- **Ferramenta de ML**: [Orange Data Mining](https://orange.biolab.si/) (treinamento e avaliação visual de modelos).

## 📊 Resultados e Métricas

Foram testados diversos algoritmos de regressão para prever a variável alvo ``tempo_de_entrega``. Abaixo, o desempenho dos principais modelos nos dados de teste:

| Modelo            | MSE   | RMSE | MAE  | R²   |
|-------------------|-------|------|------|------|
| Random Forest     | 20.66 | 4.54 | 3.07 | 0.773|
| Linear Regression  | 37.84 | 6.15 | 4.51 | 0.584|
| kNN (k=3)        | 49.57 | 7.04 | 4.71 | 0.456|
| kNN (k=5)        | 49.50 | 7.03 | 4.63 | 0.457|
| kNN (k=7)        | 50.37 | 7.07 | 4.64 | 0.447|
| SVM               | 72.33 | 8.50 | 6.51 | 0.206|

**Conclusão:** O modelo **Random Forest** apresentou o melhor desempenho, explicando aproximadamente **77%** da variabilidade dos dados (R² = 0.773) e com o menor erro médio absoluto (MAE), errando, em média, cerca de 3 dias para mais ou para menos.

## 🚀 Como Executar

1. Clone o repositório:
```bash
    git clone https://github.com/seu-usuario/olist-delivery-time-ml.git
```

2. Instale as dependências:
```bash
    pip install -r requirements.txt
```

3. Certifique-se de que os arquivos CSV originais do Olist estão na pasta ``data/raw/``.

4. Execute o script de preparação dos dados:
```bash
    python prepare_data.py
```
Isso irá gerar o arquivo ``orders_features.csv`` na pasta ``data/processed/``.

6. Execute a Modelagem no Orange:

    - Abra o **Orange Data Mining**.

    - Vá em **File > Open** e selecione o arquivo ``orange_workflow/olist_workflow.ows``.

    - No widget "File" , dê um duplo clique e localize o arquivo gerado anteriormente: ``data/processed/orders_features.csv``.

    - O fluxo será executado automaticamente, treinando os modelos e exibindo os resultados.

## 🎥 Vídeo de apresentação

[![Apresentação do projeto](https://img.youtube.com/vi/SEU_VIDEO_ID_AQUI/0.jpg)](https://www.youtube.com/watch?v=SEU_VIDEO_ID_AQUI)

## 👤 Autora

**Laís Brum**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/laisbrme/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lais-brum/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:eng.laisbm@gmail.com)