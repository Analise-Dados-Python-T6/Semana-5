"""
AULA 3 - Numpy no catálogo da Netflix
Arrays, operações vetorizadas e broadcasting aplicados a um catálogo de filmes.
"""

import numpy as np

titulos = np.array(
    [
        "Aurora Boreal",
        "Código Vermelho",
        "O Último Verão",
        "Risada Solta",
        "Noite sem Fim",
        "Planeta Azul",
        "Perseguição Final",
        "Cartas para Ana",
    ]
)
categorias = np.array(
    ["Drama", "Ação", "Drama", "Comédia", "Terror", "Documentário", "Ação", "Romance"]
)
anos = np.array([2019, 2021, 2020, 2022, 2018, 2023, 2021, 2020])
notas = np.array([7.6, 5.6, 6.8, 5.1, 6.1, 7.8, 6.3, 6.6])
duracao_min = np.array([118, 121, 106, 99, 94, 88, 115, 104])
views_milhoes = np.array([12.4, 28.6, 8.1, 15.3, 6.7, 3.9, 34.2, 19.8])


# 1. CRIANDO ARRAYS A PARTIR DO CATÁLOGO
print(notas)
print(type(notas))
print("shape:", notas.shape)


# 2. ARRAY 2D E SHAPE: VIEWS POR REGIÃO
print()
regioes = np.array(["América do Norte", "América Latina", "Europa e Ásia"])
views_por_regiao = np.array(
    [
        [4.9, 5.2, 2.3],
        [9.1, 7.4, 12.1],
        [3.2, 2.8, 2.1],
        [5.0, 6.7, 3.6],
        [2.4, 2.1, 2.2],
        [1.3, 1.0, 1.6],
        [11.8, 9.0, 13.4],
        [6.1, 8.3, 5.4],
    ]
)
print(regioes)
print(views_por_regiao)
print("shape:", views_por_regiao.shape)


# 3. LISTA PYTHON VS ARRAY NUMPY
print()
notas_lista = [7.6, 5.6, 6.8, 5.1, 6.1, 7.8, 6.3, 6.6]
print(notas_lista * 2)

print(np.array(notas_lista) * 2)


# 4. FUNÇÕES PRONTAS PARA CRIAR ARRAYS
print()
print(np.zeros(8))
print(np.arange(2018, 2024))
print(np.random.default_rng(42).integers(1, 6, size=8))


# 5. INDEXAÇÃO E SLICING
print()
print(titulos[0])
print(titulos[-1])
print(notas[1:4])
print(anos[:3])


# 6. ESTATÍSTICAS BÁSICAS
print()
print("soma das notas:", round(notas.sum(), 2))
print("nota média:", round(notas.mean(), 2))
print("menor nota:", notas.min())
print("maior nota:", notas.max())
print("desvio padrão:", round(notas.std(), 2))
print("duração média (min):", round(duracao_min.mean(), 2))


# 7. OPERAÇÕES VETORIZADAS NA PRÁTICA
print()
receita = views_milhoes * 250000
print("receita publicitária estimada (R$ 0,25 por visualização):", receita.round(2))
print("receita total:", round(receita.sum(), 2))
print("com reajuste de 8%:", (receita * 1.08).round(2))
print("duração em horas:", (duracao_min / 60).round(2))


# 8. MÁSCARAS BOOLEANAS
print()
bem_avaliados = notas >= 7.5
print(bem_avaliados)
print(titulos[bem_avaliados])
print(notas[bem_avaliados])
print(np.where(notas >= 7.5, "Em alta", "No catálogo"))


# 9. BROADCASTING COM ESCALAR
print()
pontos_recomendacao = notas * 10 + 5
print(pontos_recomendacao)


# 10. BROADCASTING ENTRE MATRIZ E VETOR
print()
peso_regiao = np.array([1.4, 0.7, 1.0])
views_ponderadas = views_por_regiao * peso_regiao
print(views_ponderadas.round(2))
print("total por título:", views_ponderadas.sum(axis=1).round(2))

media_por_regiao = views_por_regiao.mean(axis=0).round(2)
for regiao, media in zip(regioes, media_por_regiao):
    print(regiao, media)


# 11. ERRO REAL - SHAPES INCOMPATÍVEIS
print()
try:
    print(notas + peso_regiao)
except ValueError as erro:
    print("ERRO:", erro)
