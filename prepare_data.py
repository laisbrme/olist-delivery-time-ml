'''
Preparação dos arquivos de dados para modelagem de tempo de entrega.

Este script realiza as seguintes etapas:
1. Carrega os dados brutos dos arquivos CSV.
2. Agrega informações relevantes dos itens do pedido.
3. Une as tabelas em um único DataFrame.
4. Calcula o tempo de entrega em dias como variável alvo.
5. Extrai features temporais do timestamp de compra.
6. Seleciona colunas úteis e salva o DataFrame final em um novo arquivo CSV

Resultado:
- orders_features.csv: Contém as features preparadas para modelagem.

'''

# Importação das bibliotecas
import pandas as pd
from datetime import datetime

# Carregamento dos dados
customers = pd.read_csv("data/customers.csv")
geoloc = pd.read_csv("data/geolocation.csv")
order_items = pd.read_csv("data/order_items.csv")
payments = pd.read_csv("data/order_payments.csv")
orders = pd.read_csv("data/orders.csv", parse_dates=["order_purchase_timestamp","order_delivered_customer_date","order_estimated_delivery_date"])
products = pd.read_csv("data/products.csv")

# Agregação dos itens do pedido
items_agg = order_items.groupby("order_id").agg(
    n_items=("order_item_id","count"),      # número de itens por pedido
    total_price=("price","sum"),            # soma dos preços
    total_freight=("freight_value","sum"),  # soma do frete
    avg_price=("price","mean")              # preço médio
).reset_index()

# Uni as tabelas em um único DataFrame 
df = orders.merge(customers, on="customer_id", how="left").merge(items_agg, on="order_id", how="left").merge(payments.groupby("order_id").agg(
    payment_value=("payment_value","sum"),      # valor total pago
    n_payments=("payment_installments","count") # número de pagamentos
).reset_index(), on="order_id", how="left")

# Calcula o tempo de entrega em dias
df = df.dropna(subset=["order_purchase_timestamp","order_delivered_customer_date"])
df["tempo_de_entrega"] = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.total_seconds() / 86400.0

# Extrai features temporais do timestamp de compra
df["purchase_dayofweek"] = df["order_purchase_timestamp"].dt.dayofweek
df["purchase_hour"] = df["order_purchase_timestamp"].dt.hour
df["purchase_month"] = df["order_purchase_timestamp"].dt.month

# Diferença entre data estimada e data real de entrega
df["diff_estimated_days"] = (df["order_estimated_delivery_date"] - df["order_delivered_customer_date"]).dt.total_seconds() / 86400.0

# Seleciona colunas úteis e salva em CSV
cols = ["order_id","tempo_de_entrega","n_items","total_price","total_freight","avg_price","payment_value","n_payments","customer_state","purchase_dayofweek","purchase_hour","purchase_month","diff_estimated_days"]
df[cols].to_csv("data/processed/orders_features.csv", index=False)
