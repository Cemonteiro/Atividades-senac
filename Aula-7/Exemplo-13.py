import os
os.system('cls' if os.name == 'nt' else 'clear')

numero_1 = int(input("informe um numero: "))
numero_2 = int(input("informe um numero: "))

valor_da_soma = numero_1 + numero_2

valor_da_subtraçao = numero_1 - numero_2

valor_da_multiplicaçao = numero_1 * numero_2

valor_da_divisao = numero_1 / numero_2

print (f" Valor somado: {valor_da_soma = }")
print (f" Valor subtraido: {valor_da_subtraçao}")
print (f"Valor multiplicado: {valor_da_multiplicaçao}")
print (f"Valor dividido: {valor_da_divisao}")