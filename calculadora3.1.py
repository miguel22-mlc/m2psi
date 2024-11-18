x="sim"
while x=="sim":
    n1=float(input("introduza o 1º valor: "))
    n2=float(input("introduza o 2º valor: "))
    operacao=input("Qual operação deseja realizar? soma, subtração, multiplicação, divisão ou somatorio: ")
    if operacao=="soma":
        resultado=n1+n2
    elif operacao=="subtração":
        resultado=n1-n2
    elif operacao=="multiplicação":
            resultado=n1*n2
    elif operacao=="divisão":
            resultado=n1/n2
    elif operacao=="somatorio":
        resultado=0
        if n1>n2:
            incremento=-1
            i1=int(n1)
            i2=int(n2)
        else:
            incremento=1
            i1=int(n1)
            i2=int(n2)
        for i in range(i1,i2+1,incremento):
            resultado= i+resultado
    else:
        print("Operação Invalida.")
        resultado=None
    if resultado is not None:
        print(f"A {operacao} dos numeros é igual a {resultado}")
    x=input("deseja fazer outra conta? sim ou não: ")