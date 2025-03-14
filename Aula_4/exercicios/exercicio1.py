validacao = "ATCG"
complementar = {"A": "T", "T": "A", "C": "G", "G": "C"}
cadeia = input("Insira uma cadeia de DNA: ").upper()
# cadeia = "".join(filter(lambda letra: letra in validacao, cadeia))
cadeia = "".join(char for char in cadeia if char in validacao)
cadeiac = "".join(complementar[char] for char in cadeia)
print("Cadeia original formatada:", cadeia)
print("Cadeia complementar:", cadeiac)