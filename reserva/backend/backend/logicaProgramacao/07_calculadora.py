num1 = int( input ("digite um numero :" ))
num2 = int (input ("digite um numero :" ))

operacao = input("escolha uma operacao (+,-,*,/):")
match operacao :
    case "+": 
      soma = num1 + num2
      print("soma", soma)

    case "/":
      divisao = num1/num2
      print("divisao", divisao)

    case "-":
      subtracao = num1 - num2
      print("subtracao", subtracao)

    case "*":
      multiplicacao = num1 * num2
      print("multiplicacao ", multiplicacao)

