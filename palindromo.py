palavra=input("insira uma palavra:")
aocontrario=""
for i in range(len(palavra)-1,-1,-1):
    aocontrario= aocontrario + palavra[i]
if palavra == aocontrario:
    print("e um palindromo")
else:
    print("nao e um palindromo")
