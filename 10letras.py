contar=0
contar2=0
while contar2<10:
    letra=input("introduza uma letra: ")
    letra=letra.strip()
    if len(letra)!=1:
        print("Erro! Introduza apenas uma letra")
        continue
    else:
        if letra in "aeiouAEIOU":
            contar=contar+1
        contar2=contar2+1
print(f"Voce introduziu {contar} vogais")
