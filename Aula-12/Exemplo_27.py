import os
os.system('cls')

produto1 = ["maçã", 0.30]
produto2 = ["pera", 0.75]
produto3 = ["kiwi", 0.98]
compras = []
while True:
    produto = input("produto: ")
    if produto == "fim":
        break
    quantidade = int(input("quantidade: "))
    compras.append ([produto,quantidade])
    soma = 0.0 
    for lista in compras:
        print(f"")