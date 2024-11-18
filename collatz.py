n=int(input("Introduza um numero: ")) 
contar=0
while n!=1:
    print(int(n))
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
    contar=contar+1
print(f"1\nForam necessarios {contar} passos ate chegar ao 1")
