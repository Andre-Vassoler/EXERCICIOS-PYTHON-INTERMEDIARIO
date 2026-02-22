# EXERCICIO COM FUNÇÕES
"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o totoal para uma variável e mostre o valor
"""

def multiplicacao(*args):
    total = 1   #se começarmos com 0, ele vai multiplicar tudo por zero e acabar resultando em 0
    for numero in args:
        total *= numero
    return total

numeros = 1, 2, 3, 4, 5, 6, 7, 8    #tupla
multiplica =  multiplicacao(*numeros)
print(multiplica)

"""
Crie uma função que fala se um número é par ou impar
Retorne se o número é par ou impar
"""

def par_impar(int_n):
    if int_n % 2 == 0:
        print(f"O número {int_n} é : par")
    else:
        print(f"O número {int_n} é: ímpar")

n = input("Digite um número: ")
int_n = int(n)
par_impar(int_n)

# ou podemos fazer assim:
def impar_par(numero_int):
    multiplo_de_dois = numero_int % 2 == 0
    if multiplo_de_dois:
        return f"{numero_int} é par"
    else:
        return f"{numero_int} é ímpar"

numero = input("Digite um número: ")
numero_int = int(numero)
print(impar_par(numero_int))