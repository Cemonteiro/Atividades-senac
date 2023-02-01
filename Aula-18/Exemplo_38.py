import os
os.system('cls')

class Operacao:
    def __init__(self,valor,numero_conta, nome_cliente,tipo):
        self.valor = valor
        self.nome_cliente = nome_cliente    
        self.numero_conta =numero_conta
        self.tipo = tipo 

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
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
            self.__operacoes.appende(Operacao)


    def depositar(self,valor):
        self.saldo = self.saldo + valor
        print (self.saldo)
        operacao = Operacao(valor,self.numero,self.cliente.nome,'deposito')
        self.__Operacao.appende(Operacao)
        
def main():
    cliente = Cliente("luiz","867737272")
    conta = Conta(cliente,200,"23949291")
    conta.resumo ()

    conta.depositar(100)
    

    conta.sacar(50)
    

    print("executando código")

if __name__ =='__main__':
    main()    