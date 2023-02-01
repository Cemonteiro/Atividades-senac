import os
os.system('cls')

class Vendedor:
    def __init__(self,nome, telefone):
        self.nome = nome
        self.telefone = telefone
class Produto:
    def __init__(self, produto_nome, preco, estoque, descricao, vendedor):
        self.produto_nome = produto_nome
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao
        self.vendedor = vendedor
class Venda:
    def __init__(self,vendedor, produto, quantidade):
        self.vendedor = vendedor
        self.produto = produto
        self.quantidade = quantidade

nome_vendedor = input(f"informe seu nome: ")
telefone_vendedor = input(f"informe seu telefone: ")



vendedor = Vendedor(nome_vendedor, telefone_vendedor)
lista_produtos = []

while True:
    cadastro = str(input(f"Deseja cadastrar, vender ou sair: "))
    if cadastro == "c": 
            nome_produto = input(f"informe o produto que deseja cadastra: ")
            preco_produto = input (f"informe o preço do produto:")
            estoque_Produto = input(f"informe o estoque: ")
            descricao_produto = input("informe uma descrição para o produto: ")
            produto = Produto(nome_produto,preco_produto,estoque_Produto, descricao_produto, vendedor)
            lista_produtos.append (produto)
    elif cadastro == "v":
        # print (lista_produtos[0].produto_nome)
        print (lista_produtos[0].preco)
        print (lista_produtos[0].estoque)
        print (lista_produtos[0].descricao)
        print (lista_produtos[0].vendedor.nome)
        for produto in lista_produtos:
            indice = lista_produtos.index(produto)
            print(f"{indice} - {produto.produto_nome}")

        input(f"Qual produto voce deseja realizar uma venda: ")
    elif cadastro == "s":
        break
