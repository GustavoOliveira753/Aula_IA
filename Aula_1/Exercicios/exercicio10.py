temp = int(input("Insira o tempo gasto na viagem:"))
velmed = int(input("Insira a velocidade média do automóvel durante a viagem:"))

dist = velmed*temp

qtdecomb = dist/12

print("Quantidade de combustível utilizada na viagem: %.2f" % qtdecomb)
print("Distância percorrida pelo automóvel na viagem:", dist)