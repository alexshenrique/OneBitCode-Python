import pprint



gamesDict = {
    "resident evil 4":{
        "yearLaunched": 2023,
        "classification": 9.8,
        "genre": ["ação", "aventura"]
    },
    "mario odyssey":{
        "yearLaunched": 2017,
        "classification": 10,
        "genre": ["aventura", "3d"]
    
    },
    "donkey kong country":{
        "yearLaunched": 1995,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionário
print(gamesDict["mario odyssey"]["classification"])

# 2 - Adicionar um novo jogo
gamesDict["super mario bros."]["players"] = 1
print(gamesDict["super mario bros."])

# 3 - Remover um jogo
del gamesDict["resident evil 4"]
pp.pprint(gamesDict)