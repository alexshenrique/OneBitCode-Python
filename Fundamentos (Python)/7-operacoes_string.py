gameDescription = """
Fifa 23 é um jogo eletrônico de esportes de futebol desenvolvido pela EA Sports.
O jogo foi lançado em 2023, com a entrada gratuita para todos os jogadores.
"""

gameName = "Fifa"
gameVersion = "23"
line = "="

# Operação de concatenar strings
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicar strings
print(line * 50)

# 3 - Procura palavra dentro de uma string
print("Fifa" in gameDescription)
print("futebol" in gameDescription)