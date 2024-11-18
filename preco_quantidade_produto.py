preco=1000 

quantidade=int(input("Insira quantos vai comprar:")) 

ppg=quantidade*preco 

if quantidade>=500 and quantidade<=1000: 

    d5p=ppg*0.95 

    d5=ppg*0.05 

    print(f"quantidade:{quantidade}, preco a pagar {d5p}€ e desconto de 5% de {d5}€") 

elif quantidade>1000: 

    d8p=ppg*0.92 

    d8=ppg*0.08 

    print(f"quantidade:{quantidade}, preco a pagar {d8p}€ e desconto de 8% de {d8}€") 

elif quantidade<500: 

    print(f"nao a desconto tu vai pagar {ppg}€") 