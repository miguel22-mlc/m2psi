for i in range(9,18):
    temp=float(input(f"Qual a temperatura as {i} horas: "))
    if i==9:
        maior=temp
        menor=temp
    if temp<ultima:
        if temp<menor:
            menor=temp
    if temp>ultima:
        if temp>maior:
            maior=temp  
    ultima=temp
amplitude=maior-menor
print(f"A amplitude e {amplitude}℃")
