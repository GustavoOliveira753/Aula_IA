sal = float(input("Digite o salário do funcionário:"))
func = input("Digite o nome do funcionário:")
inss = sal*0.08
ir = sal*0.15
saltot = sal-(inss+ir)

print("Boas-vindas", func)
print("Valor do INSS", inss)
print("Valor do IR", ir)
print("Salário:", saltot)