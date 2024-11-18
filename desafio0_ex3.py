qnt_alunos=int(input("Insira quantos alunos tem a turma: "))
melhor_media=0
n_aluno=-1
for i in range(1,qnt_alunos+1):
    media=float(input(f"Introduza a media do aluno de nº{i}: "))
    if media>=melhor_media:
        melhor_media=media
        n_aluno=i
print(f"O aluno com a melhor media e o de nª{n_aluno}.")