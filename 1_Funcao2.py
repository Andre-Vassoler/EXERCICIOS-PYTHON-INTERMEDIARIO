# EXERCICIO COM FUNÇÕES
"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
"""

print("DUPLICADOR, TRIPLICADOR E QUADRUPLICADOR".center(50, "!"))
numero = input("Digite um número: ")
int_numero = int(numero)

def duplica(int_numero):
    dobro = 2 * int_numero
    return f"O dobro de {numero} é: {dobro}"

def triplica(int_numero):
    triplo = 3 * int_numero
    return f"O triplo de {numero} é: {triplo}"

def quadruplo(int_numero):
    quatro = 4 * int_numero
    return f"O quadruplo de {numero} é: {quatro}"
    
print(duplica(int_numero))
print(triplica(int_numero))
print(quadruplo(int_numero))

## para deixar mais simples:

def duplica(int_numero):
    return f"O dobro de {numero} é: {int_numero * 2}"

def triplica(int_numero):
    return f"O triplo de {numero} é: {int_numero * 3}"

def quadruplo(int_numero):
    return f"O quadruplo de {numero} é: {int_numero * 4}"


print(duplica(int_numero))
print(triplica(int_numero))
print(quadruplo(int_numero))