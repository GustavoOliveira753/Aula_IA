def carregarAlunos():
    alunos = []
    notas = []

    for i in range(5):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        print()

        alunos.append(nome)
        notas.append(nota)
    
    # resultado = []
    # resultado.append(alunos)
    # resultado.append(notas)
    # return resultado
    return [alunos,notas]
def nomeAlunoMaiorNota(matriz):
    # implementar e retornar o nome do aluno e a maior nota
    # alunos = matriz[0]
    # notas = matriz[1]
    # maiornota = notas[0]
    # for i in range(5):
    #     if maiornota<=notas[i]:
    #         maiornota=notas[i]
    #         pos = i
    # return [alunos[pos], notas[pos]]
    alunos = matriz[0]
    notas = matriz[1]
    nota = notas[0]
    for i in range(5):
        if nota<=notas[i]:
            aluno = alunos[i]
            nota = notas[i]
    return [aluno, nota]
print("Exemplo 2")
matriz = carregarAlunos()
maiornota = nomeAlunoMaiorNota(matriz)
print(f"O aluno {maiornota[0]} tem a maior nota, que é {maiornota[1]}")