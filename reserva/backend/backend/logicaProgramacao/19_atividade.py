import json
produto = []
categoria = []

id_categoria = 0
id_produto = 0

def exibir_menu():
    print(".........loja eletronico.........")
    print("1.Cadastrar Categoria")
    print("2.listar categoria")
    print("3.categoria associada")
    print("4.sair")

def cadastrar_categoria():
     print("/cadastrar produto:")
     nome_categoria = input ("Nome: ")
     id_categoria +=1

     armazem_categoria = {
          "nome_categoria" : nome_categoria,
          "id_categoria" : id_categoria
     }
     
def cadastrar_produto():
     id_produto +=1
     nome_produto = input ("nome:")
     preco = input ("preco:")
     id_categoria_associada = input

     armazem_produto = {
     "nome_produto" : nome_produto,
          "id_produto" : id_produto,
          "preco ": preco ,
          "id_categoria_associada " : id_categoria_associada,}
     
while True:
    exibir_menu()
    opcao = input("escolha uma opção: ")

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        cadastrar_produto()
    elif opcao == '3':
            listar_produtos()
    elif opcao == '4':
            print("Encerrando sistema. Até logo!")
            break
    else:
            print("Opção inválida. Tente novamente.")



    
     