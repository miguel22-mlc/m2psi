#sequencia fatorial
qnt=int(input("Deseja saber o fatorial do nº: "))
n=1
for i in range(1,qnt+1):
    n=n*i
print(f"o fatorial de {qnt} é {n}")