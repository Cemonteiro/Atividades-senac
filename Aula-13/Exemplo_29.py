import os
os.system('cls')

d = {"maça": [10,0.30],"pera": [10, 0.75], "kiwi":[10, 0.98]}
 
pdt = input("qual produto desejado: maça,pera, kiwi ")
busca = d.get(pdt)
print(busca)

if busca in d:
    qte = float(input("informe a quantidade da compra: "))
    busca <= d[0]
    busca = busca * qte
    print(busca)
