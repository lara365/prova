import json
produto = []
categoria = []

id_categoria = 0
id_produto = 0

def carregar_arquivo(eletronico):
    try:
        with open(eletronico, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Arquivo {eletronico} carregado!")
            return dados
    except FileNotFoundError:
        print(f"Arquivo não encontrado. Criando novo arquivo.")
        return []


def exibir_menu():
    print(".........loja eletronico.........")
    print("1.Cadastrar Categoria")
    print("2.cadastrar produto")
    print("3.listar produto")
    print("4.sair")

def cadastrar_categoria():
    global id_categoria
    print("/cadastrar produto:")
    nome_categoria = input ("Nome: ")
    id_categoria +=1

    armazem_categoria = {
        "nome_categoria" : nome_categoria,
        "id_categoria" : id_categoria
     }

    categoria.append(armazem_categoria)
    print("salvo")
     
def cadastrar_produto():
    global id_produto
    id_produto +=1
    nome_produto = input ("nome:")
    preco = input ("preco:")
    id_categoria_associada = input

    armazem_produto = {
        "nome_produto" : nome_produto,
        "id_produto" : id_produto,
        "preco ": preco ,
        "id_categoria_associada " : id_categoria_associada,}
     
def listar_produtos():
    if not produto:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    


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