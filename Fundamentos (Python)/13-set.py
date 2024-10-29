gamesSet = {"Fifa 23", "Red Dead 2", "Star Wars", 
            "Mario Odyssey", "The Legend of Zelda"}

print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)


# 3 - Adicionar um novo item
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)

# 3- Não possibilita recuperar valores via fatiamento ou slice
