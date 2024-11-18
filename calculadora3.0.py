x="sim"
while x=="sim":
    n1=float(input("introduza o 1º valor: "))
    n2=float(input("introduza o 2º valor: "))
    operacao=input("Qual operação deseja realizar? soma, subtração, multiplicação ou divisão: ")
    if operacao=="soma":
        print("A soma dos numeros é igual a", n1+n2)
    elif operacao=="subtração":
        print("A adição dos numeros é igual a", n1-n2)
    elif operacao=="multiplicação":
        print(f"A adição dos numeros é igual a", n1*n2)
    elif operacao=="divisão":
        print(f"A adição dos numeros é igual a", n1/n2)
    else:
        print("Operação Invalida.")
    x=input("deseja fazer outra conta? sim ou não: ")