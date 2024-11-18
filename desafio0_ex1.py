n1=float(input("Introduza um numero: "))
n2=float(input("Introduza um numero: "))
if n1==n2:
    print("Os numeros são iguais")
elif n1>n2:
    diferenca=n1-n2
    print(f"OS numeros sao diferentes e a sua diferenca e de {diferenca}")
else:
    diferenca=n2-n1
    print(f"OS numeros sao diferentes e a sua diferenca e de {diferenca}")