"""
faça um programa para imprimir:
1
2   2
3   3   3
4   4   4   4
...
n   n   n   n   n...    n
Para um n informado pelo usuário.
Use uma função que receba um Valor 
n inteiro e imprima até a n-ésima linha
"""
def enes(n):
    for c in range(1, n + 1):
        cont = 1
        while True:
            print(c, end=' ')
            if cont == c:
                break
            cont += 1
        print()
        
        
n = int(input('Digite um número: '))
enes(n)     
