arr = []
intervalo = 0
for i in range(10):
    arr.append(int(input("Digite um número intiro: ")))
for nm in arr:
    if nm>=10 and nm<=20:
        intervalo += 1
print("Número no intervalo de 10 a 20:", intervalo)