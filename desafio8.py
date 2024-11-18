bacterias=int(input("QUantas bacterias tem no final da experiencia: "))
dias=0
resto=1
while resto!=0:
    bacterias=bacterias/2
    dias=dias+1
    resto=bacterias%2
print(f"No começo da experiencia tinham {bacterias} bacterias e a experiencia decorreu em {dias} dias.")
