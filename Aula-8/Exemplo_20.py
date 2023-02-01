import os
os.system('cls' if os.name == 'nt' else 'clear')
'''
Escreva um programa que leia números
inteiros do teclado. O programa deve ler os números até que o usuário
digite 0. No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética
'''
contador = 0
resultado = 0
while True: 
    numero_digitado = int(input("informe um número: "))
    resultado = resultado + numero_digitado
    if numero_digitado == 0:
        break
    contador += 1
print (f" Quantidade de numeros digitados: {contador}")
print (f"Soma dos numeros digitados: {resultado}")
print (f" Média aritmética: {resultado /contador}")