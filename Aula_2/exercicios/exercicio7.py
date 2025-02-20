arr = []
maior = 0
menor = 999999999999999
media = 0

print(menor)

for i in range(10):
    arr.append(int(input("Insira as idades dos alunos: ")))
for i in arr:
    if i >= maior:
        maior = i
    if i <= menor:
        menor = i
media = (maior+menor)/2
print("Maior número:", maior)
print("Menor número:", menor)
print("Media dos números:", media)