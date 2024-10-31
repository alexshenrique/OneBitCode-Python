#EX 1
# Calculo da Distancia



#EX 2
#Aumento de Salario

salario = float(input("Digite o seu salário atual: "))

# Calculando o Novo Salario

if salario > 1250:
    novo_salario = salario * 0.1
    print(f"Seu novo salário com aumento é: {salario + novo_salario}")
elif salario <= 1250:
    novo_salario = salario * 0.15
    print(f"Seu novo salário com aumento é: {salario + novo_salario}")
    

