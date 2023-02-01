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
def exercicio_1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Digite um número: '))
exercicio_1(n)