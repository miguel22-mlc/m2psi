alfabeto="qwertyuiopasdfghjklçzxcvbnm"
alfabeto_m=alfabeto.upper()
numeros="1234567890"
simbolos="!#$%&=?+*_\\/-.:,;@£§€"
senha=input("Introduza uma senha para vefificar se ela é segura: ")
lmin=False
lmai=False
n=False
tamanho=False
simb=False
for x in alfabeto_m:
    if x in senha:
        lmai=True
        break
for x in alfabeto:
    if x in senha:
        lmin=True
        break
for x in numeros:
    if x in senha:
        n=True
        break
for x in simbolos:
    if x in senha:
        simb=True
        break
if len(senha)>=8:
    tamanho=True
if lmin==True and lmai==True and tamanho==True and simb==True and n==True:
    print(f"A sua senha é segura, {senha}")
else: 
    print("A sua senha é invalida, não é segura")
    if lmin==False:
        print("A sua senha não tem letras minusculas")
    if lmai==False:
        print("A sua senha não tem letras maiusculas")
    if simb==False:
        print("A sua senha não tem Caracteres Especiais")
    if n==False:
        print("A sua senha não tem numeros")
    if tamanho==False:
        print("A sua senha é muito pequena")