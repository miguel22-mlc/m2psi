a=-1
b=-1
c=-1
while a<0 or b<0 or c<0:
    a=float(input("Introduza um lado do triangulo: "))
    b=float(input("Introduza outro lado do triangulo: "))
    c=float(input("Introduza outro outro lado do triangulo: "))
    if a>0 and b>0 and c>0:
        if (a+b)>c and (b+c)>a and (a+c)>b:
            if a==b and b==c:
                print("É um triangulo Equilatero")
            elif (a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a):
                print("É um triangulo Isosceles")
            elif a!=b and a!=c and b!=c:
                print("É um triangulo Escaleno")
        else:
                print("Não é um triangulo")
    else:
         print("Um triangulo NÃO pode ter lados NEGATIVOS. Introduza a seguir SOMENTE valores POSITIVOS")