# digitar minha idade 

idade = int(input("Digita sua idade: "))

if idade >= 18:
   print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
#Descrição: Peça ao usuário para digitar um número inteiro.

numero = int(input("Digite um número inteiro: ")) 

if numero > 0:
   print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
   # Descrição: Usando um loop for, exiba os números de 10 a 1 em ordem decrescente
   
for  numero in range(10, 0, -1):
    print(numero)

#Descrição: Peça ao usuário para digitar um número. Usando um loop for, exiba a
#tabuada desse número de 1 a 10.

numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
   
   #Descrição: Peça ao usuário para digitar números repetidamente. O programa deve somar esses números.



soma_total= 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma_total += numero 

print(f"A soma total dos números digitados é: {soma_total}")

#Descrição: Crie um número secreto (por exemplo, 5). Peça ao usuário para tentar adivinhar o número.


numero_secreto = 5
tentativa = None 

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar o número secreto: ")) 
    
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.") 
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns, você acertou!")

# Crie uma lista inicial com alguns itens de mercado (por exemplo, ["maçã","banana", "leite"]).



itens_mercado = ["maçã", "banana", "leite"]
print(f"Lista de itens de mercado: {itens_mercado}")

novo_item = input("Adicione um novo item à lista: ")
itens_mercado.append(novo_item)  # O novo item é adicionado ao final da lista
print(f"Lista atualizada de itens de mercado: {itens_mercado}")

# Crie uma lista de números inteiros (por exemplo, [10, 5, 20, 8, 15]).


numeros = [18,9, 90, 9, 79]
maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número na lista é: {maior_numero}")


