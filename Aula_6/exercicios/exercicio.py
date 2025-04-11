def calcular_total_venda(linhas):
    for linha in linhas:
        yield int(linha[1])*float(linha[2])
    
arquivo = open("Aula_6/exercicios/vendas.txt", 'r')
linhas = arquivo.readlines()
linhas = [linha.strip("\n") for linha in linhas]
linhasArr = [linha.split(";") for linha in linhas]
totalVendas = round(sum(calcular_total_venda(linhasArr)), 2)
for linha in linhasArr:
    print(f"Produto: {linha[0]} - Total: R$ {round((int(linha[1]) * float(linha[2])) ,2)}")
print(f"\nTotal Geral: R$ {totalVendas}")