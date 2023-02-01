quantidade_de_notas_de_cinquenta = 0    
quantidade_de_notas_de_vinte = 0   
quantidade_de_notas_de_dez = 0
quantidade_de_notas_de_um = 0
while True:
    valor_digitado = input("informe o valor que deseja sacar (digite zero (0) para sair: ")
    if not valor_digitado.isdecimal():
        print ("Valor invalido! Digite um numero inteiro. ")
        continue
    valor_digitado = int(valor_digitado)
    if valor_digitado == 0:
        print ('Até mais!')
    quantidade_de_notas_de_cinquenta = int(valor_digitado / 50)
    resultado = int(valor_digitado % 50)

    quantidade_de_notas_de_vinte = int(valor_digitado / 20)
    resultado = int(valor_digitado % 20)

    quantidade_de_notas_de_dez = int(valor_digitado / 10)
    resultado = int(valor_digitado % 10)

    quantidade_de_notas_de_um = int(valor_digitado / 1)
    resultado = int(valor_digitado % 1)
    break
if quantidade_de_notas_de_cinquenta:
    print (f"{quantidade_de_notas_de_cinquenta} 
     ")