mesas=10
cadeiras=mesas*5
while cadeiras>0 and mesas>0:
    clientes=int(input("Quantos clientes entraram no restaurante:"))
    if clientes>cadeiras:
        print("nao tem lugares disponiveis")
        break
    mesas=mesas-1
    cadeiras=cadeiras-clientes
    print(f"Ainda tem {mesas} de mesas livres, e {cadeiras} de lugares livres")
if cadeiras==0 or mesas==0:
    print("O restaurante está cheio")