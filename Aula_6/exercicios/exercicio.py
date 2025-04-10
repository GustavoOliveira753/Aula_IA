def calcular_total_venda(linhas):
    
arquivo = open("Aula_6/exercicios/vendas.txt", 'r')
linhas = arquivo.readlines()
linhas = [linha.strip("\n") for linha in linhas]
linhasArr = [linha.split(";") for linha in linhas]
print(linhasArr)