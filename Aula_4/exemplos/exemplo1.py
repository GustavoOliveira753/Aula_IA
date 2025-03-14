alunos = ["Felipe", "Isabele", "Pedro", "Ligia", "Matheus"]

print(alunos)
print(f"O primeiro valor do vetor é {alunos[0]}")
print(f"O ultimo valor é {alunos[4]}")
print(f"O ultimo valor é {alunos[-1]}")

for nome in alunos:
    print(nome)
print()
for i in range(5):
    print(f"Na posição {i} tem o valor {alunos[i]}")