arr = []
i = 0
while True:
    i = int(input("Insira um número (insira -1 para parar): "))
    if i != -1:
        arr.append(i)
    else:
        break
# numeros = ''.join([str(char) for char in arr])
numeros_str = ''.join(map(str, arr))
soma = sum(arr)
media = soma/len(arr)
maiormedia = [x for x in arr if x >= media]
menormedia = [x for x in arr if x < media]
print("Quantidade de valores lidos:", len(arr))
print("Valores na ordem que foram informados um ao lado do outro:", numeros_str)
print("Soma dos valores:", soma)
print("Media dos valores:", media)
print("Quantidade de valores acima da média:", len(maiormedia))
print("Quantidade de valores abaixo da média:", len(menormedia))