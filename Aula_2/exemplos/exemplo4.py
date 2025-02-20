soma = 0
for i in range(5):
    nota = float(input("Digite a nota " + str((i+1)) + ": "))
    soma += nota
media = soma / 5
print("Soma de todas as notas:", soma, "\nMedia de todas as notas:", media)