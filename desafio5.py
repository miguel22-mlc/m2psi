contarX=0
contarY=0
voto="OLA"
while voto!="0":
    voto=input("Introduza o voto. Lista X (vote: X) ou Lista Y (Vote: Y): ")
    if voto in ("Y","y"):
        contarY=contarY+1
    elif voto in ("X","x"):
        contarX=contarX+1
if contarX>contarY:
    print(f"A Lista X venceu!!!\nCom {contarX} votos.")
elif contarY>contarX:
    print(f"A Lista Y venceu!!!\nCom {contarY} votos.")