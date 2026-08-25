dia = int(input("digite um número de 1 a 7: "))
match dia:
  case 1:
      print("domingo")
  case 2:
      print("segunda-feira")
  case 3:
      print("terça-feira")
  case 4:
      print("quarta-feira")
  case 5:
        print("quinta-feira")
  case 6:
      print("sexta-feira")
  case 7:
      print("sábado")
  case _:
      print("numero inválido! Digite um número de 1 a 7")