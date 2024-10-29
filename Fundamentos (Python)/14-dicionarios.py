gameFifa = {
    "name": "Fifa 23",
    "yearLaunched": 2023,
    "gamePrice": 49.99,
    "classification": "8.5",
    "genre": ["esporte", "familia"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do dicionário com chave e valor
print(gameFifa.items())