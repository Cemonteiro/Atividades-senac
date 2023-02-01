import os
os.system('cls' if os.name == 'nt' else 'clear')

segundos_em_uma_hora = 3600
dias_em_horas = 24

dia = int(input("informe a quantidade de dias: "))
hora = int(input("informe a quantidade de horas: "))
segundos = int(input("informe a quantidade de segundos: "))

segundos_nos_dias = dia * dias_em_horas * segundos_em_uma_hora
segundos_nas_horas = hora * segundos_em_uma_hora

qtetotal = segundos_nos_dias + segundos_nas_horas + segundos

print("-"*40)
print(f"a quantidade total de segundos é {qtetotal}")
print("-"*40)