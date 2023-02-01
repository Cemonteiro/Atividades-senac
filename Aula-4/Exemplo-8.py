nome = input ("informe seu nome: ")
telefone = input("informe seu numero: ")
opçao = input("deseja cadastra produto ou serviço: ")

if (opçao == "produto"):
    nome_produto = input("informe o nome do produto: ")
   
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Categoria: {opçao}")
    print(f"Produto:{nome_produto} ")
   

elif (opçao == "serviço"):

    descriçao_do_serviço = input ("informe a descrição do serviço: ")

    print(f"Nome: {nome}")
    print (f"Telefone: {telefone}") 
    print (f"Categoria: {opçao}")
    print (f"Descrição do serviço: {descriçao_do_serviço}")
else: 
    print("opçao invalida")
