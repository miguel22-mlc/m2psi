tempo=0
voltas=int(input("Quantas voltas tem a corrida: "))
for i in range(1,voltas+1):
    minutos=int(input(f"Quanto tempo(minutos) demorou a {i}º volta: "))
    tempo=tempo+minutos
print(f"Demorou {tempo} minutos para o competidor terminar a corrida")