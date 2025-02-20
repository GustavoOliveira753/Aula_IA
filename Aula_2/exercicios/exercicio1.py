numeros = []
for i in range(10):
    numeros.append(int(input("Insira o numero " + str(i+1) + ": ")))
maior = 0
menor = 0
for nm in numeros:
    if nm>=10:
        maior+=1
    else:
        menor+=1
print("Quantidade de numeros maiores ou iguais a 10:", maior)
print("Quantidade de numeros menores que 10:", menor)