pontos=12
opcao=0
cleve=0
cgrave=0
cmgrave=0
while opcao!="4":
    opcao=input("O condutor cometeu uma infração:\n Muito Grave(1)\n Grave(2)\n Leve(3)\n Terminar(4)\n ")
    if opcao=="1":
        cmgrave=cmgrave+1
        pontos=pontos-6
    elif opcao=="2":
        cgrave=cgrave+1
        pontos=pontos-4
    elif opcao=="3":
        cleve=cleve+1
        if cleve>1:
            pontos=pontos-1
    if cgrave+cmgrave==2 or cgrave==2 or pontos<=0 :
        print("O condutor perdeu a carta")
    print(f"O condutor esta com {pontos} pontos na carta.")
