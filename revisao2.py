unidades=int(input("Quantas unidades do produto voce vai comprar: "))
precoproduto=float(input("Quanto custa o produto: "))
if unidades<=10:
    preco=unidades*10
elif unidades>10 and unidades<=20:
    uni=unidades-10
    desconto=precoproduto-(precoproduto*0.05)
    preco=(uni*desconto)+(10*precoproduto)
elif unidades>20:
    uni=unidades-20
    desconto=precoproduto-(precoproduto*0.10)
    desconto5=precoproduto-(precoproduto*0.05)
    preco=(10*precoproduto)+(uni*desconto)+(10*desconto5)
print(f"voce vai pagar {preco}€ por {unidades} de um produto que custa {precoproduto}€")
