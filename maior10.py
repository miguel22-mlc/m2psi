for i in range(10):
    n=int(input("Introduza um numero:"))
    if i==0:
        maior=n
    else:
        if n>maior:
          maior=n
         posicao=i+1
print(f"O maior e o {maior} e foi o {posicao}º a ser inserido")
