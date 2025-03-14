validacao = "ATCG"
cadeia = input("Insira uma cadeia de DNA: ").upper()
cadeiac = ""
# cadeiaf = "".join(filter(lambda letra: letra in validacao, cadeia))
cadeiaf = ''.join([char for char in cadeia if char in validacao])
for char in cadeiaf:
    if char in "A":
        cadeiac = "".join("T")
    if char in "T":
        cadeiac = "".join("A")
    if char in "C":
        cadeiac = "".join("G")
    if char in "G":
        cadeiac = "".join("C")

print("Cadeia original formatada:", cadeiaf)
print("Cadeia complementar:", cadeiac)