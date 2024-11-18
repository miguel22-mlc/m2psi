import random  

x=random.randint(1,10) 

n1=int(input("Adivinhe, o numero secreto: ")) 

if n1==x: 

    print("Acertou o numero!!!") 

elif x<n1: 

    print("é menor") 

elif x>n1: 

    print("e maior") 

if x<n1 or x>n1: 

     n2=int(input("Tente outro numero: ")) 

     if n2==x: 

         print("Acertou o numero!!!") 

     elif x<n2: 

         print("e menor") 

     elif x>n2: 

         print("e maior") 

     if x>n2 or x<n2: 

         n3=int(input("Tente outro numero: ")) 

         if n3==x: 

            print("Acertou o numero!!!") 

         else: 

             print(f"errou, o numero secreto era {x}") 