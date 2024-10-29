gameList = ["Resident Evil 4", "Star Wars Jedi Survivor",
            "The Legend of Zelda", "Red Dead Redemption 2","Mario Odyssey", "Uncharted 4"]

# 1 - Tamanho da lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo indice
print(gameList.index("Star Wars Jedi Survivor"))

# 3 - Adicionar um item ao final da lista
gameList.append("Final Fantasy VII")
print(gameList)

# 4 - Ordernar a lista 
gameList.sort()
print(gameList)

# 5 - Copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("The Legend of Zelda")
print(gameReset)