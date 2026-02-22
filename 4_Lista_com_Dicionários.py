# EXERCICIO:
"""
Aumente os preços dos produtos a seguir em 10%
gere novos produtos poor deep copy (cópia profunda)
"""
produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]
"""
Ordene os produtos por nome decrescente( do maior para o menor)
Gere os produtos ordenados por nome por deep copy (cópia profunda)

Ordene os produtos por preço crescente (do menor para o maior)
Gere os produtos ordenados por preço por deep copy (cópia profunda)
"""
import copy

print("TABELA COM REAJUSTE DE 10%")
novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto["preco"] *= 1.10
    produto["preco"] = round(produto["preco"], 2)   # 2 casas decimais

for produto in novos_produtos:
    print(f"{produto["nome"]}: {produto["preco"]}")


print("\nTABELA ORDENADA POR NOME")
produtos_ordenado_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenado_por_nome.sort(key=lambda p: p["nome"], reverse=True)
# lambda é basicamente uma função anônima (sem nome), usada para coisas simples e rápidas
for produto in produtos_ordenado_por_nome:
    print(f"{produto["nome"]}: {produto["preco"]}")


print("\nTABELA ORDENADA POR PREÇO")
produtos_ordenado_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenado_por_preco.sort(key=lambda p:p["preco"])

for produto in produtos_ordenado_por_preco:
    print(f"{produto["nome"]}: {produto["preco"]}")