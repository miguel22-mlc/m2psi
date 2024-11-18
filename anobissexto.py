ano=int(input("Introduza um ano: "))
if (ano%4==0 and ano%100!=0) or ano%400==0:
    print(f"O ano inserido {ano} é Bissexto")
else:
    print("O ano não é bissexto")