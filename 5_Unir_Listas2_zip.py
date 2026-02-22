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


li1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
li2 = ["BA", "SP", "MG"]

print(list(zip(li1, li2)))