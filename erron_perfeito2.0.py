n=int(input("Introduza um numero: "))
soma_divisores=0
divisores=0
while soma_divisores!=n:
    divisores=divisores+1
    if n%divisores==0:
        soma_divisores=soma_divisores+divisores
    if soma_divisores>n:
        print("O numero não é perfeito")
        break
if soma_divisores==n:
    print("O numero é perfeito")