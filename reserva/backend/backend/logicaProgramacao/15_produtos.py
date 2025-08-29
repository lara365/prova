import json 
inventario = []
try:
    with open('loja.json','r') as arquivo:
        inventario = json.load(arquivo)
        print ("Arquivo carregador !")
except FileNotFoundError:
    print("arquivo nao encontrado")

print("n----cadstrar produto----")
nome_produto = input("digite o nome do produto:")

while True:
    try:
        quantidade = int(input("digite a quatidade"))
        break
    except ValueError:
        print("digite apenas numeros")
while True:
    try:  
        preco =float(input("Digite o preço")) 
        break
    except ValueError:
        print("Digite o preço corretamente")

novo_produto = {
    "nome_produto": nome_produto,
    "quantidade": quantidade,
    "preco":preco,
    "tem_estoque": quantidade > 0
}

# escrever no arquivo json
inventario.append(novo_produto)
with open('loja.json','w')as arquivo:
    json.dump(inventario,arquivo,indent=4)

    print(f"\n produto{nome_produto}foi cadastrado")
