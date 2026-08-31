TempoHora = int(input("digite a hora: "))
Mts = int(input("digite os minutos: "))

Tempo_segundos = (TempoHora*3600) + (Mts*60)
print(f"O total em segundos: {Tempo_segundos}s.")