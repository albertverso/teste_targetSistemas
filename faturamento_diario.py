import json

# Exemplo de JSON com valores de faturamento
faturamento_json = '''
{
    "faturamento_diario": [1500, 2300, 0, 1800, 2500, 2700, 0, 3000, 1000, 0, 0, 2000, 1900, 2700, 2300, 2900, 0, 2100, 3200]
}
'''

faturamento = json.loads(faturamento_json)["faturamento_diario"]

def calcular_faturamento(faturamento):
    faturamento_validos = [dia for dia in faturamento if dia > 0]  # Ignorar dias sem faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)
    dias_acima_da_media = sum(1 for dia in faturamento_validos if dia > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento(faturamento)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")