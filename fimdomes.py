dia=int(input("Insira o dia: "))
mes=int(input("Insira o mês: "))
ano=int(input("insira o ano: "))
if mes in (1,3,5,7,8,10,12):
    falta=31-dia
elif mes==2:
    if (ano%4==0 and ano%100!=0) or ano%400==0:
        falta=29-dia
    else:
        falta=28-dia
elif mes in (4,6,9,11):
    falta=30-dia
print(f"Faltam {falta} dias para o fim do mes")
