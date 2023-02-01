import os
os.system('cls' if os.name == 'nt' else 'clear')

qte_km = int(input("informe a quantidade de quilometros percorridos: "))
qte_dia = int(input("informe a quantidade de dias de aluguel: "))

valor_km = qte_km * 0.15 
valor_dia = qte_dia * 60

valor_final = f'{valor_km:.2f}' + f'{valor_dia:.2f}'.replace(".",",")




print(f"O preço a pagar será: R$ {valor_final}")



