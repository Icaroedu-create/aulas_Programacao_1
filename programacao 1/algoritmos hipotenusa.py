print("=== calculo en triangulo rentangulo ===")
print("1 - calcular hipotenusa")
print("2 - calcular cateto")

opcao = int(input("escolha uma opcao: "))

if opcao == 1:
    cateto1 = float(input("digite o valor do cateto 1: "))
    cateto2 = float(input("digite o valor do cateto 2: "))
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    
    print(f"o valor da hipotenusa é: {hipotenusa:.2f}")
    
elif opcao == 2:
    hipotenusa = float(input("digite o valor da hipotenusa: "))
    cateto1 = float(input("digite o valor do cateto 1: "))
    
    if hipotenusa > cateto1:
        outro_cateto = (hipotenusa ** 2 - cateto1 ** 2) ** 0.5
        print(f"\no valor do outro cateto é: {outro_cateto:.2f}")
    else:
        print("\nO valor da hipotenusa deve ser maior que o cateto 1.")
else:
    print("\nOpção inválida.")
        