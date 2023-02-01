import os
os.system('cls')

produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
produto_desejado = input(f"qual produto desejado? ")
quantidade_produto = input(f"informe a quantidade: ")
for lista in compras:
    print(f"produto: {lista[0]}")
    print(f"quantidade: {lista[1]}")
    print(f"preço: {lista[2]:5.2f}")