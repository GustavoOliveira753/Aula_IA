nome = input("Insira seu nome completo: ")
nomelista = nome.split(" ")
abreviacoes = [palavra[0]+'.' for palavra in nomelista[1:len(nomelista)-1]]
primeiro_nome = nomelista[0]
ultimo_nome = nomelista[-1]
print("Nome abreviado:")
print(f"{primeiro_nome.capitalize()} {' '.join(abreviacoes)} {ultimo_nome.capitalize()}")