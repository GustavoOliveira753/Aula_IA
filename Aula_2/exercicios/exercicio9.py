vmonteiro = 0
veuclides = 0
neutros = 0
ganhador = ""

for i in range(10):
    voto = int(input("Insira o número dos candidatos (10-Monteiro Lobato, 35-Euclides da Cunha, 0-neutro): "))
    if voto==10:
        vmonteiro+=1
    elif voto==35:
        veuclides+=1
    else:
        neutros+=1
if vmonteiro>veuclides:
    ganhador = "Monteiro Lobato"
elif veuclides>vmonteiro:
    ganhador = "Euclides da Cunha"
else:
    ganhador = "Empate ou mais votos nulos"
print(f'O ganhador foi: {ganhador}\nA quantidade de votos para o Monteiro Lobato foram: {vmonteiro}\nA quantidade de votos para o Euclides da Cunha foram: {veuclides}\nA quantidade de votos nulos foi de: {neutros}')