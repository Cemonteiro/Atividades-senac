#escreva uma função que obtém uma lista de números e uma string.
#Essa função deve retornar a string no plural caso a quantidade de números na lista seja maior que um.
#caso a lista seja vazia retorne a string sem ser manipulada.
#Ex: func([1,2,3], "adicionando") == "adicionados"
#fun ([1], "adicionado") == "adicionado"
import os
os.system('cls')
def funcao (lista,resultado):
    if len(lista) > 1:
        print(f"{resultado}s")
    else:
        print(resultado)
funcao  ([1,2,3,4], "adicionado")
funcao ([1], "adicionado")
