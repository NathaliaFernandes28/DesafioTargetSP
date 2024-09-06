# Valores de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento.values())

# Cálculo do percentual de representação de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

# Exibição dos resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
