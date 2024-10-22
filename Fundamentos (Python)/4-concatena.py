name = input("Qual o nome do jogo?\n")
yearLaunch = int(input("Em que ano foi lançado?\n"))
gamePrice = float(input("Qual o preço do jogo?\n"))
planIncluded = bool(input("Possui plano incluso?\n"))

print("### Dados do Jogo ###")
print("=====================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano de Lançamento:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Plano Incluso:", planIncluded)

# Alternativa 2
# print("Nome do Jogo:", name, "\nAno de Lançamento:", yearLaunch, "\nPreço do Jogo:", gamePrice, 
#       "\nPlano Incluso:", planIncluded)

# Alternativa 3
print(f"Nome do Jogo: {name} \nAno de Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nPlano Incluso: {planIncluded}")