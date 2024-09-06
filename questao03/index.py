
faturamento_diario = [
    22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 
    42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 
    2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 
    18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 
    13220.495, 8414.61
]


faturamento_validos = [valor for valor in faturamento_diario if valor > 0]


menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)


media_mensal = sum(faturamento_validos) / len(faturamento_validos)


dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)


print(f"Menor valor de faturamento ocorrido em um dia do mês: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")
