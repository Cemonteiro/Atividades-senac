# Algoritmo de média de notas

nota1 = float(input("escreva nota 1: "))
nota2 = float(input("escreva nota 2: "))
nota3 = float(input("escreva nota 3: "))

media= (nota1 + nota2 + nota3) /3

print("media e :", + media)

if media >= 7:
        print("Aprovado")
else:
        print("Reprovado")