n1=float(input("introduza o 1º valor: "))
n2=float(input("introduza o 2º valor: "))
operacao=input("Qual operação deseja realizar? soma, subtração, multiplicação ou divisão: ")
if operacao=="soma":
       resultado=n1+n2
elif operacao=="subtração":
       resultado=n1-n2
elif operacao=="multiplicação":
        resultado=n1*n2
elif operacao=="divisão":
        resultado=n1/n2
else:
        print("Operação Invalida.")
        resultado=None
if resultado is not None:
    print(f"A {operacao} dos numeros é igual a {resultado}")
  