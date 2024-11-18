outramusica="sim"
musica=22
tempo=0
while outramusica=="sim":
    outramusica=input("Deseja colocar uma musica, sim ou nao? ")
    if outramusica=="sim":
         musica=int(input("Introduza o tempo da musica em segundos:"))
    else:
        break
    if musica==0:
        break
    if musica<0 or musica>=6000:
        print("a musica nao pode ter essa duraçao")
        continue
    tempo=tempo+musica
talbum=tempo//60
segundos = tempo%60
print(f"A duração do album é {int(talbum)}m:{int(segundos)}s")