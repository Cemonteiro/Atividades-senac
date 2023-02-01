d = {"maça": 0.30,"pera": 0.75, "kiwi": 0.98}
 
pdt = input("qual produto desejado: maça,pera, kiwi ")
busca = d.get(pdt)
print(busca)

if busca != None:
    qte = float(input("informe a quantidade da compra: "))
    busca = busca * qte
    print(busca)