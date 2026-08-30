"""
MINI-DESAFIO: ELETRÔNICOS POR LOJA
Qual loja teve mais vendas de Eletrônicos, e qual o ticket médio nela?

Este arquivo mostra 3 formas diferentes de chegar na mesma resposta:
1. groupby() com duas chamadas separadas (a forma "direta", vista na aula)
2. groupby().agg() com múltiplas métricas de uma vez só
3. pivot_table() como alternativa ao groupby
"""

import pandas as pd #importar biblioteca

vendas = pd.read_csv("vendas.csv") #pd.read_
vendas["quantidade"] = vendas["quantidade"].fillna(1) #precnher quantidade =1 nas linhas vazias

eletronicos = vendas[vendas["categoria"] == "Eletrônicos"]  #Verificando se a categoria é eletronico


# ---------------------------------------------------------------
# FORMA 1: groupby() simples, uma chamada para cada métrica
# ---------------------------------------------------------------
print("FORMA 1: groupby() separado para contagem e média")

contagem_por_loja = eletronicos.groupby("loja")["id_venda"].count()  #agrupando cada um dos tipos de loja a partir do id de venda
ticket_medio_por_loja = eletronicos.groupby("loja")["preco_unitario"].mean().round(2) #agrupando cada uma das lojas e trazendo a média dos preços (com 2 casas decimais)

print("Quantidade de vendas de Eletrônicos por loja:")
print(contagem_por_loja)
print("\nTicket médio (preço unitário) por loja:")
print(ticket_medio_por_loja)

contagem_ordenada = contagem_por_loja.sort_values(ascending=False) #ordenando/listando a contagem de cada loja (do maior para o menor)
loja_mais_vendas_1 = contagem_ordenada.index[0] #mostrando apenas o mais vendido
print(f"\n>> Loja com mais vendas: {loja_mais_vendas_1} "
      f"({contagem_ordenada.iloc[0]} vendas, "
      f"ticket médio R$ {ticket_medio_por_loja[loja_mais_vendas_1]:.2f})") 


# ---------------------------------------------------------------
# FORMA 2: groupby().agg() com nomes de coluna definidos na hora
# Vantagem: contagem e média saem juntas, numa única tabela.
# ---------------------------------------------------------------
print("FORMA 2: groupby().agg() combinando as duas métricas")

resumo = eletronicos.groupby("loja").agg(
    qtd_vendas=("id_venda", "count"),
    ticket_medio=("preco_unitario", "mean"),
).round(2)

resumo_ordenado = resumo.sort_values("qtd_vendas", ascending=False)
print(resumo_ordenado)

loja_mais_vendas_2 = resumo_ordenado.index[0]
print(f"\n>> Loja com mais vendas: {loja_mais_vendas_2} "
      f"({resumo_ordenado.loc[loja_mais_vendas_2, 'qtd_vendas']} vendas, "
      f"ticket médio R$ {resumo_ordenado.loc[loja_mais_vendas_2, 'ticket_medio']:.2f})")

# ---------------------------------------------------------------
# FORMA 3: pivot_table() como alternativa ao groupby
# Útil quando já se está acostumado a pensar em "tabela dinâmica".
# ---------------------------------------------------------------
print("FORMA 3: pivot_table() com count e mean lado a lado")

piv = eletronicos.pivot_table(
    index="loja",
    values="preco_unitario",
    aggfunc=["count", "mean"],
).round(2)
piv.columns = ["qtd_vendas", "ticket_medio"]

piv_ordenado = piv.sort_values("qtd_vendas", ascending=False)
print(piv_ordenado)

loja_mais_vendas_3 = piv_ordenado.index[0]
print(f"\n>> Loja com mais vendas: {loja_mais_vendas_3} "
      f"({piv_ordenado.loc[loja_mais_vendas_3, 'qtd_vendas']} vendas, "
      f"ticket médio R$ {piv_ordenado.loc[loja_mais_vendas_3, 'ticket_medio']:.2f})")


resumo.to_csv("piv.csv")

# ---------------------------------------------------------------
# As três formas devem chegar exatamente na mesma resposta.
# ---------------------------------------------------------------
