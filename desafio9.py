montante=float(input("Introduza a quantia que deseja investir: "))
juros=float(input("Introduza a taxa de Juro anual liquida: "))
anos=int(input("Introduza quantos anos dura o seu investimento: "))
juros=juros/100
for i in range(anos):
    montante=montante*(1+juros)
    print(f"O montante do {i+1}º ano é de {montante}€")
    