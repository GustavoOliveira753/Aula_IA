arr = []
fx110 = 0
fx1117 = 0
fx18 = 0

for i in range(10):
    arr.append(int(input("Insira as idades das pessoas: ")))
for i in arr:
    if i >=1 and i <=10:
        fx110+=1
    elif i >=11 and i <= 17:
        fx1117+=1
    else:
        fx18+=1
print("Quantidade de pessoas na faixa de 1 a 10 anos:",fx110)
print("Quantidade de pessoas na faixa de 11 a 17 anos:",fx1117)
print("Quantidade de pessoas que tem 18 anos ou mais:",fx18)