arr = []
impar=0
pares=0
for i in range (10):
    arr.append(int(input("Insira um número inteiro: ")))
for n in arr:
    if n % 2 == 0:
        pares+=1
    else:
        impar+=1
print("Numero pares:", pares)
print("Numero impares:", impar)