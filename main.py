import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- Carregar dataset ---
df = pd.read_csv('Games.csv')

# --- Converter Sales para numérico ---
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# --- Converter Release para datetime (tentando parsing flexível) ---
df['Release'] = pd.to_datetime(df['Release'], errors='coerce', format='%b-%y')

# --- Filtrar os 15 jogos mais vendidos ---
top15 = df.sort_values(by='Sales', ascending=False).head(15)

# ====================
# GRÁFICO 1: BARRAS - VENDAS POR JOGO
# ====================
plt.figure(figsize=(12, 6))
plt.bar(top15['Name'], top15['Sales'], color='skyblue')
plt.title('Top 15 Jogos Mais Vendidos')
plt.xlabel('Jogo')
plt.ylabel('Vendas (milhões)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ====================
# GRÁFICO 2: LINHAS - VENDAS AO LONGO DO TEMPO (Top 15)
# ====================
top15_sorted_by_date = top15.dropna(subset=['Release']).sort_values(by='Release')
plt.figure(figsize=(12, 6))
plt.plot(top15_sorted_by_date['Release'], top15_sorted_by_date['Sales'], marker='o', linestyle='-')
plt.title('Vendas dos Top 15 ao Longo do Tempo de Lançamento')
plt.xlabel('Data de Lançamento')
plt.ylabel('Vendas (milhões)')
plt.grid(True)
plt.tight_layout()
plt.show()

# ====================
# GRÁFICO 3: PIZZA - DISTRIBUIÇÃO POR GÊNERO
# ====================
plt.figure(figsize=(8, 8))
top15['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribuição por Gênero - Top 15 Jogos')
plt.ylabel('')
plt.tight_layout()
plt.show()
