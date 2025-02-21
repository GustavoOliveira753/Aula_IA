valor = float(input("Digite o valor da prestação"))
juro = float(input("Insira a taxa de juros em porcentagem"))/100
atraso = int(input("Digite o tempo de atraso em dias"))

taxa = (juro**2)

prest = valor+(valor*taxa*atraso)

print("Valor da prestação:", prest)