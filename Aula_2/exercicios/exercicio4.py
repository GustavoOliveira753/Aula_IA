arr = []
qtde = 0
soma = 0
media = 0

for i in range(10):
    arr.append(int(input("Insira um número inteiro: ")))

for i in arr:
    if i >= 70 and i <= 90:
        qtde+=1
        soma+=i
media = soma / qtde
print("Quantidade:", qtde)
print("Soma dos números:", soma)
print("Média dos números:", media)