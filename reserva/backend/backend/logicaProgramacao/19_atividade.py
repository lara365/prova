import json

produto = []
categoria = []

id_categoria = 0
id_produto = 0

def carregar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Arquivo {nome_arquivo} carregado!")
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Criando novo arquivo.")
        return []

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
        print(f"Arquivo {nome_arquivo} salvo.")

def exibir_menu():
    print(".........loja eletronico.........")
    print("1.Cadastrar Categoria")
    print("2.cadastrar produto")
    print("3.listar produto")
    print("4.sair")

def cadastrar_categoria():
    global id_categoria
    print("/cadastrar categoria:")
    nome_categoria = input("Nome: ")
    id_categoria += 1

    armazem_categoria = {
        "nome_categoria": nome_categoria,
        "id_categoria": id_categoria
    }

    categoria.append(armazem_categoria)
    salvar_arquivo("categorias.json", categoria)
    print("salvo")

def cadastrar_produto():
    global id_produto
    id_produto += 1
    nome_produto = input("nome: ")
    preco = input("preco: ")

    print("categorias disponíveis:")
    for item in categoria:
        print(item["id_categoria"], "-", item["nome_categoria"])

    id_categoria_associada = int(input("categoria: "))

    armazem_produto = {
        "nome_produto": nome_produto,
        "id_produto": id_produto,
        "preco": preco,
        "id_categoria_associada": id_categoria_associada
    }

    produto.append(armazem_produto)
    salvar_arquivo("produtos.json", produto)
    print("salvo")

def listar_produtos():
    if not produto:
        print("Nenhum produto cadastrado.")
        return

    for item_produto in produto:
        nome_categoria_encontrado = "Categoria não encontrada"

        for item_categoria in categoria:
            if item_categoria["id_categoria"] == item_produto["id_categoria_associada"]:
                nome_categoria_encontrado = item_categoria["nome_categoria"]
                break

        print(f"ID do Produto: {item_produto['id_produto']}")
        print(f"  Nome: {item_produto['nome_produto']}")
        print(f"  Preço: R$ {item_produto['preco']}")
        print(f"  Categoria: {nome_categoria_encontrado}")
        print()


categoria = carregar_arquivo("categorias.json")
produto = carregar_arquivo("produtos.json")


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
