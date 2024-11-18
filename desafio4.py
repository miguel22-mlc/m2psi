peso=0
valor_mala=0
while peso<1000:
    peso_mala=int(input("Qual o peso da mala?: "))
    peso=peso+peso_mala
    valor_mala=valor_mala+20
if peso==1000:
    print(f"O avião chegou ao limite de peso, e o valor arrecadado em malas é de {valor_mala}.")
elif peso>1000:
    print("O avião ultrapassou o limite de peso possivel para carregar.")
