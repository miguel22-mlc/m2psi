diasano=0
dia=int(input("Insira o dia: "))
mes=int(input("Insira o mês: "))
ano=int(input("insira o ano: ")) 
for i in range(mes,13):
    if i in (1,3,5,7,8,10,12):
        diasmes=31
    elif i==2:
        if (ano%4==0 and ano%100!=0) or ano%400==0:
            diasmes=29
        else:
            diasmes=28
    elif i in (4,6,9,11):
            diasmes=30
    diasano=diasano+diasmes
faltaa=diasano-dia
print(f"Faltam {faltaa} dias para o final do ano")   
      