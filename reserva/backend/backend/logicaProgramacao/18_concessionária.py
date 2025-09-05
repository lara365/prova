# eu como um dono de concessionaria de carros importados, preciso de um sistema
# para controlar meu estoque de veiculos. para me organizar melhor
# além do nome gostaria de guardar o ano, quilometragem, marca, preço, cor e quantidade de cada veiculo
#quero um menu, onde eu possa cadastrar, alterar, excluir e listar meus veiculos. para me sentir especial
#quero o nome da minha loja apareça no topo do menu
#moya´s imports

import json

arquivo_banco = 'biblioteca.json'

def carregar_dados():
    try:
        with open(arquivo_banco, 'r') as arq:
            return json.load(arq)
    except FileNotFoundError:
        print(" Arquivo não encontrado. Um novo será criado.")
        return []

def salvar_dados(livros):
    with open(arquivo_banco, 'w') as arq:
        json.dump(livros, arq, indent=4)

def mostrar_menu():
    print("="*40)
    print("         BIBLIOTECA CENTRAL")
    print("="*40)
    print("1. Cadastrar novo livro")
    print("2. Listar todos os livros")
    print("3. Buscar por título")
    print("4. Excluir livro")
    print("5. Sair")
    print("="*40)

def cadastrar_livro(livros):
    print("\n---- Cadastrar Livro ----")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    editora = input("Editora: ").strip()

    while True:
        try:
            ano = int(input("Ano de publicação: "))
            break
        except ValueError:
            print("Digite um número para o ano.")

    while True:
        try:
            paginas = int(input("Número de páginas: "))
            break
        except ValueError:
            print("Digite um número para páginas.")

    genero = input("Gênero: ").strip()
    idioma = input("Idioma: ").strip()

    livro = {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "ano_publicacao": ano,
        "numero_paginas": paginas,
        "genero": genero,
        "idioma": idioma
    }

    livros.append(livro)
    salvar_dados(livros)
    print(f" Livro '{titulo}' cadastrado com sucesso!\n")

def listar_livros(livros):
    print("\n---- Lista de Livros ----")
    if not livros:
        print("Nenhum livro cadastrado.\n")
        return

    for i, l in enumerate(livros):
        print(f"[{i}] {l['titulo']} | Autor: {l['autor']} | Ano: {l['ano_publicacao']} | Páginas: {l['numero_paginas']} | Gênero: {l['genero']} | Idioma: {l['idioma']}")
    print()

def buscar_por_titulo(livros):
    termo = input("\nDigite o título ou parte dele: ").strip().lower()
    encontrados = [l for l in livros if termo in l['titulo'].lower()]

    if encontrados:
        print("\n--- Livros Encontrados ---")
        for l in encontrados:
            print(f"{l['titulo']} | Autor: {l['autor']} | Ano: {l['ano_publicacao']}")
        print()
    else:
        print(" Nenhum livro encontrado com esse título.\n")

def excluir_livro(livros):
    listar_livros(livros)
    if not livros:
        return

    try:
        i = int(input("Digite o número do livro para excluir: "))
        if i < 0 or i >= len(livros):
            print(" Índice inválido.\n")
            return

        confirm = input(f"Tem certeza que deseja excluir '{livros[i]['titulo']}'? (s/n): ").lower()
        if confirm == 's':
            excluido = livros.pop(i)
            salvar_dados(livros)
            print(f" Livro '{excluido['titulo']}' excluído com sucesso!\n")
        else:
            print(" Exclusão cancelada.\n")

    except ValueError:
        print(" Digite um número válido.\n")

livros = carregar_dados()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_livro(livros)
    elif opcao == '2':
        listar_livros(livros)
    elif opcao == '3':
        buscar_por_titulo(livros)
    elif opcao == '4':
        excluir_livro(livros)
    elif opcao == '5':
        print(" Encerrando o sistema. Até logo!")
        break
    else:
        print(" Opção inválida. Tente novamente.\n")
