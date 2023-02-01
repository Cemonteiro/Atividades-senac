#escreva um programa que compare duas listas. considerando a primeira lista como a versão inicial e 
# a segunda como a versão pós alterações. utilizando operações com conjuntos,
#seu programa devera imprimir a lista de modificações entre essas duas versões listando:
#os elementos que não mudaram
#os novos elementos 
#os elementos que foram removidos

L1 = [1,2,3,4,5]
L2 = [3,5,8,11,15]

print (f"{set(L1).intersection(set(L2))}")
print (f"{set(L1).difference (set(L2))}")
print (f"{set(L2).difference(set(L1))}")