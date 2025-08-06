nota = int (input ("digite sua nota:"))

match nota:
    case 10:
        print ("aprovado, voce tem futuro")
    case 7 |8|9:
        print ("media, voce vai ser sempre o segundo")
    case 0|1|2|3|4|5|6:
        print ("reprovado,voce vai ser um sem futuro ou um futuro clt sem ganhar o minimo")
    case _:
        print ("tente novamente se nao der certo desista")

