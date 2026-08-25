A = int(input("digite um número: "))
B = int(input("digite outro número: "))
operacao = input("digite a operação (+, -, *, /): ")

match operacao:
    case "+":
        print(A + B)
    case "-":
        print(A - B)
    case "*":
        print(A * B)
    case "/":
        if B == 0:
            print("não é possível dividir por zero")
        else:
            print(A / B)
    case _:
        resultado = "operação inválida. Digite uma operação válida (+, -, *, /)"
        
print(f"resultado: {resultado}")
