mesas=10
cadeiras=50
for _ in range(10):
    clientes=int(input("quantas pessoas entraram no restaurante"))
    mesas=mesas-1
    cadeiras=cadeiras-clientes
    print(f"Ainda tem {mesas} de mesas livres, e {cadeiras} de cadeiras livres")
    if cadeiras = 0 or mesas=0:
        break