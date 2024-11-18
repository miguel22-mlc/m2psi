a=float(input("insira um numero: "))
b=int(input("Insira outro valor: "))
c=0
d=a
for _ in range(b-1):
    c=d*a
    d=c
print(c)
