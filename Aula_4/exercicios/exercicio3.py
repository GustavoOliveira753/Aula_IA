arr1=[]
arr2=[]
for _ in range(5):
    arr1.append(int(input("Insira 5 digitos: ")))
for _ in range(5):
    arr2.append(int(input("Insira mais 5 digitos: ")))
soma = [arr1[i] + arr2[i] for i in range(5)]
produtos = [arr1[i]*arr2[i] for i in range(5)]
diferenca = [x for x in arr1 if x not in arr2]
intersecao = [x for x in arr1 if x in arr2]
uniao = list(set(arr1) | set(arr2))
print("Soma:", soma)
print("Produtos:", produtos)
print("Diferença:", diferenca)
print("Interseção:", intersecao)
print("Uniao:", uniao)