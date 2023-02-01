import os
os.system('cls' if os.name == 'nt' else 'clear')

salario = int(input("informe o salario: "))
porcentagem = int(input ("informe a porcentagem de aumento do salario: "))

salario_final = salario+(salario*(porcentagem/100))

print(f"salario final e de:{salario_final} ")