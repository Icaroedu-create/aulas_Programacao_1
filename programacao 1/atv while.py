continua = True
while continua:
    n = int(input("digite qual a tabuada: "))
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")
    
    continua = input("Deseja continuar? (s/n): ").lower() == 's'
    continua = True 