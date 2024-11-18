dinheiro=float(input("Quanto dinheiro pode gastar? "))
peso=float(input("Quanto peso pode carregar? "))
while dinheiro>0 and peso>0:
    preco=float(input("Insira o preço do produto:"))
    if preco==0:
        break
    pesop=float(input("Insira o peso do produto:"))
    if dinheiro<preco or peso<pesop:
        print("Dinheiro insuficiente ou produto muito pesado")
    else:
        dinheiro=dinheiro-preco
        peso=peso-pesop
        print(f"Ainda tem {dinheiro}$, e ainda consegue carregar {peso}")
if dinheiro==0 or peso==0:
    print("compra finalizada") 