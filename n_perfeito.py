n=int(input("Introduza um numero: "))
soma_divisores=0
for i in range(1,n):
    if n%i==0:
        soma_divisores=soma_divisores+i
if soma_divisores==n:
    print("O numero é perfeito")
else:
    print("O numero não é perfeito")