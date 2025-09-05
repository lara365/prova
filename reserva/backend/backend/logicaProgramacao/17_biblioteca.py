import json 

livros = []
try:
    with open('biblioteca.json', 'r') as arquivo:
        livros = json.load(arquivo)
        print("Arquivo carregado!")
except FileNotFoundError:
    print("Arquivo nao encontrado")

print("\n---- Cadastrar livro ----")
titulo = input("Digite o título do livro: ")

autor = input("Digite o nome do autor: ")

editora = input("Digite a editora: ")

while True:
    try:
        ano_publicacao = int(input("Digite o ano de publicação: "))
        break
    except ValueError:
        print("Digite apenas numeros para o ano.")

while True:
    try:  
        numero_paginas = int(input("Digite o número de páginas: ")) 
        break
    except ValueError:
        print("Digite apenas numeros para páginas.")

genero = input("Digite o gênero: ")
idioma = input("Digite o idioma: ")

novo_livro = {
    "titulo": titulo,
    "autor": autor,
    "editora": editora,
    "ano_publicacao": ano_publicacao,
    "genero": genero,
    "numero_paginas": numero_paginas,
    "idioma": idioma
}

# Escrever no arquivo json
livros.append(novo_livro)
with open('biblioteca.json', 'w') as arquivo:
    json.dump(livros, arquivo, indent=4)

print(f"\nLivro '{titulo}' foi cadastrado com sucesso.")

# inventario = []
#with open ("biblioteca.json", "r") as biblioteca:
# produto_para_alterar = int(input("digite o id do produto")
#inventario = json.load(biblioteca)
# for livro in inventario:
# if produto_para_alterar == livro ["id"]:
#novo_nome=input ("digite o novo nome ")
#livro["nome"]=novo_nome
#with open("biblioteca.json","w")as biblioteca:
#json.dump(inventario,biblioteca,ident=4)