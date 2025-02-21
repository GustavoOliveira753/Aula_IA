quant = int(input("Digite a quantidade dos itens:"))
val = float(input("Digite o custo do item:"))

sub = quant*val
desc = sub*0.17
tot = sub-desc

print("Valor bruto:", sub)
print("Valor do desconto:", desc)
print("Valor líquido:", tot)