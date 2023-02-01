this is a quick demo

import os
os.system('cls')
saque = 1
cedula_50 = 0
cedula_20 = 0
cedula_10 = 0 
cedula_1 = 0
while True:
    saque = input("qual valor deseja sacar: ")
    if saque.isnumeric() is True: 
        saque = int(saque)
        if saque == 0:
            break
        else:
            cedula_50 = int(saque / 50)
            resto = saque % 50

            cedula_20 = int(resto / 20 )
            resto = saque % 20
        
    else:
        print ("valor inválido!")

print (cedula_50)

