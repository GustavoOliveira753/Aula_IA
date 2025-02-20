arr = []
maior = 0
for i in range(10):
    arr.append(int(input("Insira uma idade: ")))
for i in arr:
    if i >= maior:
        maior = i
print("Maior idade:", maior)