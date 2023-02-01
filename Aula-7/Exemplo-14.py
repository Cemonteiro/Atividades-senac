import os
os.system('cls' if os.name == 'nt' else 'clear')

decisao = "s"
while decisao == "s":
    numero_1 = int(input("Informe um numero: "))
    numero_2 = int(input("Informe um numero: "))
    operaçao = input("Qual operação você deseja realizar: +|-|*|/ ")


    if operaçao == "+": 
        valor_somado = numero_1 + numero_2
        print(f"Valor da soma: {valor_somado} ")
        decisao = input("Voce deseja continuar s ou n: ")
    elif operaçao == "-":
        valor_subtraido = numero_1 - numero_2
        print (f"Valor da subtraçao: {valor_subtraido}")
        decisao = input("Voce deseja continuar s ou n: ")
    elif operaçao == "*":
        valor_multiplicado = numero_1 * numero_2
        print(f"Valor da multiplicação: {valor_multiplicado}")
        decisao = input("Voce deseja continuar s ou n: ")
    elif operaçao == "/":
        valor_dividido = numero_1 / numero_2
        print(f"Valor da divisão: {valor_dividido}")
        decisao = input("Voce deseja continuar s ou n: ")
    else: 
        print("opção invalida")






