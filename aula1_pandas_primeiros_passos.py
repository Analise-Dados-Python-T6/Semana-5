"""
AULA 1 - Pandas: primeiros passos
Series, DataFrames e leitura de dados de diferentes fontes.
"""

import pandas as pd

# ---------------------------------------------------------------
# 1. SERIES: a peça mais simples do Pandas
# ---------------------------------------------------------------
print("1. CRIANDO UMA SERIES")

notas = pd.Series(
    [8.5, 7.0, 9.2, 6.5],
    index=["Ana", "Bruno", "Carla", "Diego"]
)
print(notas)

print("\n--- Acessando valores de uma Series ---")
print(notas["Carla"])
print(notas.mean())

# ---------------------------------------------------------------
# 2. DATAFRAME: a tabela do Pandas
# ---------------------------------------------------------------
print("2. CRIANDO UM DATAFRAME A PARTIR DE UM DICIONÁRIO")

alunos = pd.DataFrame(
    {
        "nome": ["Ana", "Bruno", "Carla", "Diego"],
        "nota": [8.5, 7.0, 9.2, 6.5],
        "turma": ["A", "B", "A", "B"],
    }
)
print(alunos)

# Pergunta: se cada coluna de um DataFrame é uma Series,
# o que acontece quando pegamos apenas uma coluna dele?
print("\n--- alunos['nota'] é do tipo: ---")
print(type(alunos["nota"]))

# ---------------------------------------------------------------
# 3. CONHECENDO UM DATAFRAME: shape, columns, dtypes
# ---------------------------------------------------------------
print("3. SHAPE, COLUMNS E DTYPES")

print(alunos.shape)
print(list(alunos.columns))
print(alunos.dtypes)
# alunos.info() reúne as três respostas (mais uso de memória) em um resumo só.

# ---------------------------------------------------------------
# 4. PRIMEIRO OLHAR EM DADOS REAIS: .shape e .head()
# ---------------------------------------------------------------
print("4. LENDO O DATASET vendas.csv")

vendas = pd.read_csv("vendas.csv")
print(vendas.shape)
print(vendas.head())

# ---------------------------------------------------------------
# 5. EXPLORANDO RÁPIDO COM describe()
# ---------------------------------------------------------------
print("5. DESCRIBE()")

print(vendas[["preco_unitario", "quantidade"]].describe())
# count menor que o total de linhas já é uma pista de dados ausentes.

# ---------------------------------------------------------------
# 6. CONTANDO CATEGORIAS COM value_counts()
# ---------------------------------------------------------------
print("6. VALUE_COUNTS()")

print(vendas["loja"].value_counts())

# ---------------------------------------------------------------
# CHECKPOINT
# - Series = uma coluna com rótulos (índice)
# - DataFrame = uma tabela feita de várias Series
# - shape, columns e dtypes descrevem a tabela
# - .head() dá o primeiro raio-x dos dados
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# 7. LEITURA DE DADOS DE DIFERENTES FONTES
# ---------------------------------------------------------------
print("7. LENDO UM CSV COM read_csv")

vendas = pd.read_csv("vendas.csv")
print(vendas.head(3))

import pandas as pd
print("\n--- LENDO UM EXCEL COM read_excel (mesmos dados, outro formato) ---")
vendas_excel = pd.read_excel("vendas.xlsx")
print(vendas_excel.head(3))
# read_csv e read_excel devolvem o mesmo tipo de resultado (um DataFrame);
# só muda a função de leitura, o resto do código continua igual.

# Outras fontes seguem o mesmo espírito: leem a fonte e devolvem um DataFrame.
# pd.read_csv("dados.csv")
# pd.read_excel("dados.xlsx")
# pd.read_json("dados.json")
# pd.read_sql(query, conexao)
# pd.read_html(url)

import pandas as pd
# ---------------------------------------------------------------
# 8. SALVANDO DADOS: to_csv()
# ---------------------------------------------------------------
print("8. SALVANDO COM to_csv()")
vendas = pd.read_csv("vendas.csv")
resumo = vendas.groupby("categoria")["preco_unitario"].mean().round(2)
resumo.to_csv("resumo_categorias.csv")
print(pd.read_csv("resumo_categorias.csv"))
# to_csv() grava no disco; use index=False se não quiser salvar o índice
# numérico como uma coluna extra.

# ---------------------------------------------------------------
# 9. ERRO REAL: separador errado no CSV
# ---------------------------------------------------------------
print("9. ERRO REAL - SEPARADOR ERRADO NO CSV")
print(
    """
Se o arquivo usar ponto e vírgula (;) para separar colunas, e lermos com:
    vendas = pd.read_csv("vendas_europa.csv")
o resultado não trava, só que todas as colunas viram uma coluna só, por
exemplo shape (2, 1) e columns Index(['id;produto;preco']).

Por isso, sempre vale conferir o shape logo após ler um arquivo.

Como corrigir - informe o separador correto:
    vendas = pd.read_csv("vendas_europa.csv", sep=";")
"""
)

# ---------------------------------------------------------------
# 10. DADOS AUSENTES: o que fazer com NaN
# ---------------------------------------------------------------
print("10. ENCONTRANDO VALORES AUSENTES COM isnull()")

vendas = pd.read_csv("vendas.csv")
print(vendas.isnull().sum())

print("\n--- Tratando valores ausentes: dropna() e fillna() ---")
print("antes:", vendas.shape)
print("depois do dropna:", vendas.dropna().shape)

vendas["quantidade"] = vendas["quantidade"].fillna(1)
print("nulos em quantidade agora:", vendas["quantidade"].isnull().sum())

vendas = vendas.dropna().reset_index(drop=True)
print(vendas)
# dropna() é mais drástico (perde linhas inteiras);
# fillna() é mais cuidadoso, mas exige escolher um valor que faça sentido.
