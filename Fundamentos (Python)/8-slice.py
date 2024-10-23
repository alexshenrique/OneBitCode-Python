gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo eletrônico de esportes de futebol desenvolvido pela EA Sports.
O jogo foi lançado em 2023, com a entrada gratuita para todos os jogadores.
"""
# String[:] é uma forma de cortar uma string - indice começa na posição 0 | indice termina na posição -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a ultima posição
print(gameName[:1])

# 3 - Busque toda string da terceira até a ultima posição

print(gameName[2:])

'''
 string[inicio:fim:passo] - indice começa na posição 0 | indice final -1
 passo - determina o incremento. Por padrão esse numero é 1.
'''

# 4 - Busque toda a string de 2 em 2 caracteres

print(gameName[::2])

# 5 - Busque toda a string nos indices impares
print(gameName[1::2])

# 6 - Inverter uma string de tras pra frente

print(gameName[::-1])