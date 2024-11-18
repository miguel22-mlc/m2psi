n=float(input("Introduza um numero: "))
somatorio=0
n=n+0.5
for i in range(10):
    if i<9:
        print(n,end=", ")
    else:
        print(n, end="")
    somatorio=somatorio+n
    n=n+0.5
print(f" = {somatorio}")
