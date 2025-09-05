#uso do json 29/08
import json
inventario = []

try:
    with open('loja.json', 'r') as arquivo:
        inventario = json.load(arquivo)
        print("Arquivo carregado.")
except FileNotFoundError:
    print("Arquivo não encontrado. Iniciando um novo inventário.")

print("\n--- Cadastrar produto ---")
nome_produto = input("Digite o nome do produto: ")

#Loop para a quantidade
while True:
    try:
        quantidade = int(input("Digite a quantidade: "))
        break
    except ValueError:
        print("Digite apenas números inteiros.")

#Loop para o preço
while True:
    try:
        preco = float(input("Digite o preço: "))
        break
    except ValueError:
        print("Digite o preço corretamente.")

novo_produto = {
    "nome_produto": nome_produto,
    "quantidade": quantidade,
    "preco": preco,
    "tem_estoque": quantidade > 0 
}

inventario.append(novo_produto)

with open('loja.json', 'w') as arquivo:
    json.dump(inventario, arquivo, indent=4)

print(f" O produto {nome_produto} foi cadastrado")