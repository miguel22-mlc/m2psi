nomes="" 
passagem=1
lugares=0 
while lugares<passagem:
    lugares=int(input("Quantos lugares tem o avião: "))
    passagem=int(input("Quantas passagens foram vendidas: "))
    if passagem>lugares:
        print("Introduza os valores corretamente, não é possivel ter mais passagens vendidas do que lugares")
for i in range(1,passagem+1):
    nome=input("Introduza o nome do(a) passageiro(a): ")
    if nome=="":
        presença=i
        break
    else:
        nomes=nomes+nome+"\n"
print(f"entraram {presença} de {passagem} passagens vendidas passageiros e o nome deles são\n{nomes}")    
