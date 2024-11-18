idade=int(input("insira sua idade")) 

if idade<0 or idade>120: 

    print("idade invalida") 

elif idade>=0 and idade<=11: 

    print("Esta na Infancia") 

elif idade>=12 and idade<=20: 

    print("Esta na adolescencia") 

elif idade>=21 and idade<=75: 

    print("Esta na fase adulta") 

elif idade>=76 and idade<=120: 

    print("Esta na velhice") 