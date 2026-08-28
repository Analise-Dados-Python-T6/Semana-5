"""
AULA 2 - Filtros, groupby, merge e pivot
As operações que resolvem 90% dos problemas reais de análise de dados.
"""

import pandas as pd

vendas = pd.read_csv("vendas.csv")
vendas["quantidade"] = vendas["quantidade"].fillna(1)

# ---------------------------------------------------------------
# 1. SELECIONANDO LINHAS E COLUNAS: loc e iloc
# ---------------------------------------------------------------
print("1. SELECIONANDO COLUNAS")

print(vendas[["produto", "preco_unitario"]].head(3))
# Para renomear: vendas.rename(columns={"preco_unitario": "preco"})
# Para remover:  vendas.drop(columns=["col"])

# ---------------------------------------------------------------
# 2. CRIANDO UMA COLUNA CALCULADA E ORDENANDO COM sort_values()
# ---------------------------------------------------------------
print("2. COLUNA CALCULADA + sort_values()")

vendas["valor_total"] = vendas["preco_unitario"] * vendas["quantidade"]
top5 = vendas.sort_values("valor_total", ascending=False)
print(top5[["produto", "preco_unitario", "quantidade", "valor_total"]].head(5))
# ascending=False ordena do maior para o menor; por padrão, sort_values()
# ordena do menor para o maior.

# ---------------------------------------------------------------
# 3. LOC: selecionando por rótulo
# ---------------------------------------------------------------
print("3. LOC - SELECIONANDO POR RÓTULO")

print(vendas.loc[0:2, ["produto", "loja"]])
# loc[intervalo_de_linhas, lista_de_colunas]: o intervalo aqui inclui o último valor.

# ---------------------------------------------------------------
# 4. ILOC: selecionando por posição
# ---------------------------------------------------------------
print("4. ILOC - SELECIONANDO POR POSIÇÃO")

print(vendas.iloc[0:3, 0:3])
# iloc usa posições numéricas; o intervalo NÃO inclui o final, como em listas Python.

# ---------------------------------------------------------------
# 5. FILTROS BOOLEANOS
# ---------------------------------------------------------------

print("5. FILTRO SIMPLES: VENDAS ACIMA DE R$ 300")

caros = vendas[vendas["preco_unitario"] > 300]
print(caros[["produto", "preco_unitario"]].head())
print("total:", len(caros))

print("\n--- Múltiplas condições com & e | ---")
filtro = vendas[
    (vendas["categoria"] == "Móveis")
    & (vendas["estado"] == "SP")
]
print(filtro[["produto", "categoria", "estado"]])
print("total:", len(filtro))
# Atenção: cada condição precisa ficar entre parênteses; usamos & (e) e | (ou),
# nunca and / or.

# Pergunta pra pensar juntos: por que não podemos usar "and" no lugar de "&"
# ao combinar duas condições no Pandas?
# Dica: pense no que acontece quando comparamos uma coluna inteira, com
# centenas de linhas, ao mesmo tempo, e não apenas dois valores únicos.

# ---------------------------------------------------------------
# CHECKPOINT
# - vendas["col"] seleciona colunas
# - loc = por rótulo · iloc = por posição
# - condição dentro de [...] filtra linhas
# - & (e) / | (ou) combinam condições, sempre com parênteses
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# 6. GROUPBY: separando em grupos para responder perguntas
# ---------------------------------------------------------------
print("6. GROUPBY BÁSICO: PREÇO MÉDIO POR CATEGORIA")

print(vendas.groupby("categoria")["preco_unitario"].mean().round(2))

print("\n--- Múltiplas agregações com .agg() ---")
print(
    vendas.groupby("categoria")["preco_unitario"]
    .agg(["mean", "min", "max", "count"])
    .round(2)
)
# Dá pra nomear direto as colunas:
# .agg(media=("preco_unitario", "mean"), total=("preco_unitario", "sum"))

# ---------------------------------------------------------------
# 7. MERGE: juntando tabelas por uma chave em comum
# ---------------------------------------------------------------
print("7. MERGE COM how='inner'")

func = pd.read_csv("funcionarios.csv")
depto = pd.read_csv("departamentos.csv")

inner = func.merge(depto, on="id_departamento", how="inner")
print(inner[["nome", "id_departamento", "nome_departamento"]])
# funcionarios tem um id_departamento=99 que não existe em departamentos;
# com inner, ele some.

print("\n--- MERGE COM how='left' ---")
left = func.merge(depto, on="id_departamento", how="left")
print(left[["nome", "id_departamento", "nome_departamento"]])
# Com left, João Pires aparece mesmo sem departamento correspondente;
# o Pandas preenche com NaN.

# Tipos de join (how=...):
#   inner (padrão) -> só as linhas que existem nas DUAS tabelas
#   left           -> todas as linhas da tabela da esquerda
#   right          -> todas as linhas da tabela da direita
#   outer          -> todas as linhas de ambas, mesmo sem correspondência
#
# Antes de um merge, vale checar duplicatas na chave
# (func["id_departamento"].duplicated().sum()): chave repetida dos dois lados
# faz o resultado "explodir" em mais linhas do que o esperado.
#
# Para empilhar linhas de tabelas com as mesmas colunas (sem juntar por
# chave), use pd.concat().

# ---------------------------------------------------------------
# 8. PIVOT_TABLE: a tabela dinâmica do Pandas
# ---------------------------------------------------------------
print("8. PIVOT_TABLE: PREÇO MÉDIO POR CATEGORIA X ESTADO")

piv = vendas.pivot_table(
    index="categoria",
    columns="estado",
    values="preco_unitario",
    aggfunc="mean",
)
print(piv.round(2))
# df.pivot(index=, columns=, values=) é o irmão sem agregação: só funciona
# se houver 1 valor único por combinação linha x coluna.
# df.melt() faz o caminho inverso: transforma colunas de volta em linhas
# (largo -> longo).

# ---------------------------------------------------------------
# CHECKPOINT
# - groupby separa em grupos antes de calcular
# - merge junta tabelas por uma coluna-chave
# - how define o que acontece sem correspondência
# - pivot_table cruza duas colunas numa tabela só
# ---------------------------------------------------------------
