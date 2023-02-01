'''
listas em python
adição de itens
exclusão de itens
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')

valor_digitado = input (f"Deseja inserir um produto(p) ou serviço(s)? (digite 0 para sair)")
lista_de_produtos = []
lista_de_servico = []

if valor_digitado == "p": 
    nome_produto =  input("digite o nome do produto: ")
    lista_de_produtos.append (nome_produto)
    print (lista_de_produtos)
    
elif valor_digitado == "s":
    nome_serviço = input("digite o nome do serviço: ")
    lista_de_servico.append (nome_serviço)
    print (lista_de_servico)