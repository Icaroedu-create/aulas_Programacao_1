Tempo_hr = float(input("digite o trempo: "))
Tempo_segundo = Tempo_hr*3600
velocidade = 30 * 1000
distançia = velocidade*Tempo_segundo

print(f"A distançia pecorrida e de: {distançia:,.2f} m .")
