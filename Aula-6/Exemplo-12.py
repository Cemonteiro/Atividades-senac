import os
os.system('cls' if os.name == 'nt' else 'clear')

temperatura = int(input("informe a temperatura: "))

temp_f = ( 9 * temperatura / 5) + 32

print (temp_f)