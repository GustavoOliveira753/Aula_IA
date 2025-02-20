arr = []
for i in range(10):
    nome = input("Insira o nome do aluno: ")
    idade = int(input("Insira a idade do aluno: "))
    arr.append({"nome": nome, "idade": idade})
idademaior = max(arr, key=lambda obj : obj["idade"])
print("O aluno " + str(idademaior["nome"]) + " é o mais velho, com " + str(idademaior["idade"]) + " anos!")