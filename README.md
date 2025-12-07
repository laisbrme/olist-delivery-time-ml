# Projeto: Previsão do Tempo de Entrega de Pedidos (Brazilian E‑Commerce — Olist)

**Objetivo:** prever o tempo de entrega do pedido (em dias).

**Dataset:** [Brazilian E‑Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Ferramenta:** [Orange Data Mining](https://orangedatamining.com/)

**Linguagem:** [Python](https://www.python.org/)

## Objetivo

Prever o tempo de entrega (em dias) dos pedidos feitos na plataforma Olist, utilizando dados históricos de pedidos, produtos, vendedores e avaliações.

## Estrutura do repositório

- `data/` — pasta para armazenar os CSVs originais do Olist.
- `outputs/` — pasta para armazenar os dados preparados.
- `requirements.txt`
- `preparacao.py` — script para preparação e engenharia de features.
- `README.md`
- `LICENSE` — MIT

## Dados de entrada

Os dados originais do Olist, localizados em `data/`, utilizados no projeto são:
- `customers.csv`
- `geolocation.csv`
- `order_items.csv`
- `order_payments.csv`
- `orders.csv`
- `products.csv`

## Raciocínio do projeto

1ª Definição do alvo e tabelas envolvidas

2ª Preparação dos arquivos

3ª Modelagem no Orange Data Mining

## Instruções para reproduzir o projeto

1. Clone o repositório:
```bash
    git clone https://github.com/seu-usuario/olist-delivery-time-ml.git
```

2. Instale as dependências:
```bash
    pip install -r requirements.txt
```

3. Os dados do Olist, utilizados no projeto, encontram-se na pasta `data/`.

4. Execute o script de preparação dos dados:
```bash
    python preparacao.py
```

5. Os dados preparados serão salvos em `outputs/orders_features.csv`.

6. Abra o Orange Data Mining e carregue o arquivo `outputs/orders_features.csv` para iniciar a modelagem.

## Tecnologias utilizadas

- Visual Studio Code - editor de código 
- Python - preparação dos dados
- Pandas - manipulação de dados
- Orange Data Mining - modelagem
- Git e GitHub - controle de versão e hospedagem do código
- ChatGPT - auxílio na escrita da documentação

## Vídeo de apresentação

[![Apresentação do projeto](https://img.youtube.com/vi/SEU_VIDEO_ID_AQUI/0.jpg)](https://www.youtube.com/watch?v=SEU_VIDEO_ID_AQUI)


## Licença

MIT

## Contato

<!-- TODO
    [ ] Completar o README com as seções faltantes
 -->
