import random 
numeros="0981237465"
alfabeto="qwertyuiopasdfghjklçzxcvbnm"
alfabeto_m=alfabeto.upper()
simbolos="!#$%&=?+*_\\/-.:,;@£§€"
senha=""
for _ in range(2):
    x=random.randint(0,26)
    senha=senha+alfabeto[x]

    x=random.randint(0,26)
    senha=senha+alfabeto_m[x]

    x=random.randint(0,9)
    senha=senha+numeros[x]

    x=random.randint(0,26)
    senha=senha+alfabeto_m[x]

    x=random.randint(0,20)
    senha=senha+simbolos[x]

    x=random.randint(0,26)
    senha=senha+alfabeto[x]
print(senha)