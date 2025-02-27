print("Exemplo 2")

nome = "Gustavo"
idade = 18

print("Ola",nome,"voce tem a idade de",idade)

frase = "Ola " + nome + " voce tem a idade de " + str(idade)

frase = "Ola {} voce tem a idade de {}"

frase = f"Ola {nome} voce tem a idade de {idade}"

print(frase) 

salario = 1500.1234
frase = f"O salário é {salario:.2f}"
print(frase)