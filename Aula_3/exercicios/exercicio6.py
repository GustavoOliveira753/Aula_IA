frase = input("Digite uma frase: ")
espacos = 0
vogais = 0
vogal = "aeiou"
espacos = frase.count(" ")
vogais = sum(frase.lower().count(i) for i in vogal)
print("Quantidade de espaços em branco: ", espacos)
print("Quantidade de vogais: ", vogais)
