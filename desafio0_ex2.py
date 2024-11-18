hora=int(input("Introduza que horas sao: "))
if hora in (5,6,7):
    print("Este horario é de madrugada")
elif hora in (8,9,10,11,12):
    print("Este horario é de manha")
elif hora in (13,14,15,16,17,18,19):
    print("Este horario é de tarde")
elif hora in (20,21,22,23,0,1,2,3,4):
    print("Este horario é de noite")
else:
    print("Este horario não existe")