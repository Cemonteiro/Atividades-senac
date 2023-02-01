import os
os.system('cls')

notas = [5,6,2,9]
contador = 0 
soma = 0
numero_de_notas = len(notas)

while contador < numero_de_notas:
    soma = soma + notas[contador]
    contador += 1

print(f"{soma / numero_de_notas}")
