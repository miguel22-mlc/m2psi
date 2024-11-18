nome1=input("digite um nome:")
nome2=input("digite outro nome:")
if len(nome1)==len(nome2):
    print(nome1, "e o", nome2, "tem o mesmo tamanho")
elif len(nome1)>len(nome2):
    print(nome1, "é maior")
else:
    print(nome2, "é maior") 