arquivo = open("Aula_6/aula.txt", "r")
linhas = arquivo.readlines()
arquivo.close()
linhas = [linha.strip("\n") for linha in linhas]
print(linhas)
print("Tamanho do vetor é", len(linhas))

for linha in linhas:
    print(linha, end="")