saldo=0
opcao=None
contarL=0
while opcao!="4":
    opcao=input("Oque voce deseja realizar.\nVer Saldo(1)\nDepositar Dinheiro(2)\nLevantar Dinheiro(3)\nTerminar(4)\n: ")
    if saldo<0 and contarL>0:
        print(saldo,"€")
        opcao="2"
    if opcao=="1":
        print(f"O seu Saldo é de {saldo}€")
    elif opcao=="2":
        deposito=float(input("Quanto Dinheiro deseja Depositar: "))
        d=deposito-round(deposito,2)
        if d!=0:
            print("O valor é invalido")
            continue
        if deposito<=0 or deposito>10000:
            print("Não é posivel depositar esta quantia, limite ultrapassado. Limite de 10000€")
        else:
            saldo=saldo+deposito
            print(f"O seu saldo é de {saldo}€ ")
    elif opcao=="3":
        levantar=float(input("Quanto dinheiro deseja Levantar: "))
        d=levantar-round(levantar,2)
        if d!=0:
            print("O valor é invalido")
            continue
        if levantar<10:
            print("Não é possivel levantar essa quantia de dinheiro, so é permitido a partir de 10€")
            continue
        else:
            saldo=saldo-levantar
            print(f"O seu saldo é {saldo}€")
            contarL=contarL+1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                