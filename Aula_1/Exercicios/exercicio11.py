haula = float(input("Digite quanto vale a hora/aula do professor:"))
aulas = int(input("Digite quantas aulas o professor administra na semana:"))

sbruto = aulas*haula
sbruto2 = sbruto*6.2
inss = sbruto2*0.115
ir = (sbruto2-inss)*0.175
restante = sbruto2-inss-ir

print("Salário bruto:", sbruto)
print("Salário bruto * 6,2: %.2f" % sbruto2)
print("INSS: %.2f" % inss)
print("IR: %.2f" % ir)
print("Restante: %.2f" % restante)