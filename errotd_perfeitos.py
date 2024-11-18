n=int(input("Insira o numero limite: "))
for i in range(1,n+1):
    soma_divisores=0
    divisores=0
    while soma_divisores!=i:
        divisores=divisores+1
        if i%divisores==0:
            soma_divisores=soma_divisores+divisores
        if soma_divisores==i:
            print(i, end=" ")
        elif soma_divisores>i:
            break
        