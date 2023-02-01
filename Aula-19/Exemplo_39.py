#Crie um programa que pergunte o nome do cliente,
#o número da conta e seu saldo inicial.

#Após isso, o programa deve perguntar se o cliente deseja
#fazer um saque, depósito ou se deseja exibir o extrato.
#Se o usário digitar "fim" o programa encerra.

#input+ while/break + if/else
import os
from pickle import TRUE
os.system('cls')

class Operacao:
    def __init__(self,valor,numero_conta, nome_cliente,tipo):
        self.valor = valor
        self.nome_cliente = nome_cliente    
        self.numero_conta =numero_conta
        self.tipo = tipo 

class Cliente:
    def __init__(self, nome, n_conta):
        self.nome = nome
        self.n_conta = n_conta
class Conta:
    def __init__(self,cliente,saldo,numero):
        self.cliente = cliente
        self.saldo = saldo
        self.numero = numero
        self.__operacoes = []
    
    
    def resumo(self):
        print(f"Numero: {self.numero},Saldo: {self.saldo}, Cliente: {self.cliente.nome}")
    
    
    def sacar (self,valor):
        if self.saldo < valor: 
            print ("saldo insuficiente ")
        else: 
            self.saldo = self.saldo - valor
            print (self.saldo)
            operacao = Operacao(valor,self.numero,self.cliente.nome,'saque')
            self.__operacoes.append(operacao)


    def depositar(self,valor):
        self.saldo += valor
        self.__operacoes.append(["DEPÓSITO", valor])

Nome = input("informe seu nome: ")
numero_conta = input("informe o numero da conta: ")
saldo = (int(input("informe seu saldo: ")))
cliente = Cliente(Nome, numero_conta)
conta = Conta(cliente,saldo,numero_conta)
while True:
    acao = input ("Deposito{d}, Saque{S}, Resumo{R}: ")
    if acao == "d":
        valor_a_depositar = int(input("quanto deseja depositar: "))
        conta.depositar(valor_a_depositar)

    elif acao == "S":
        valor_de_saque = int((input("quanto deseja sacar: ")))
        conta.sacar(valor_de_saque)
    elif acao == "R":
        conta.resumo ()
    elif acao == "F":
        break


# while True:
#     if acao == Saque

#     return = saldo - saque 
