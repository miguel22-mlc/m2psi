contar_malas=0
limite_peso=1000
while limite_peso>=0:
    peso_mala=float(input("Peso da mala?: "))
    if peso_mala>limite_peso:
        break
    contar_malas=contar_malas+1
    limite_peso=limite_peso-peso_mala
    print(f"Ainda pode transportar {limite_peso}Kg")
print(f"O valor a cobrar pelo transporte das malas é de {contar_malas*20}.€")