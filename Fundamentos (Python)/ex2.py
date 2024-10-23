"""
    
    Exercicio 2:
    * Substituindo caractere repetido:
    -> Escreva um programa Python para obter uma string determinada string
    em que todas as ocorrencias de seu primeiro caractere foram alteradas para '$',
    exceto o proprio primeiro caractere.
    Ex: fifa 23 -> fi$a 23
    
    
    * Troca de caracteres:
    > Escreva um programa Python para obter uma unica string de duas strings fornecidas
    separadas por um espaço e troque os dois primeiros caracteres de cada string.
    Ex: abc xyz -> xyc abz
"""

# Exercicio 1
name = input("Digite um nome: ")

char = name[0].lower()
new_name = name.replace(char, '$')
new_game = char + new_name[1:]

print(new_game)

# Exercicio 2
st1 = 'cab'
st2 = 'zyx'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(new_st1)
print(new_st2)