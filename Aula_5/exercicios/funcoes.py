def stringToList(nomes: str, notas: str, faltas: str):
    nomesArr = nomes.split(";")
    notasArr = notas.split(";")
    faltasArr = faltas.split(";")
    return nomesArr, notasArr, faltasArr
