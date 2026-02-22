# EXERCICO: UNIR LISTAS
"""
Crie uma função zipper (como zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.

Use todos os valores da menor lista
Ex:
["Salvador", "Ubatuba", "Belo Horizonte"]    (menor lista)
["BA", "SP", "MG", "RJ"]

RESULTADO:
[("Salvador", "BA"), ("Ubatuba", "SP"), ("Belo Horizonte", "MG")]
"""

def zipper(lista1, lista2):
    lista_menor = min(len(lista1), len(lista2))
    return[(lista1[i], lista2[i]) for i in range(lista_menor)]


li1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
li2 = ["BA", "SP", "MG"]

print(zipper(li1, li2))