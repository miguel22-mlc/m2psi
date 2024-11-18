numero=int(input("Introduza um numero:"))
divisor=numero
while divisor>0:
    resto=numero%divisor
    if resto==0:
        print(divisor)
    divisor=divisor-1