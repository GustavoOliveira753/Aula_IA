numero = input("Insira um numero no formato(19992895090): ")
numero_formatado = ""
if (numero.isdigit and len(numero)==11):
    ddd = numero[:2]
    numero_formatado = f"({ddd}){numero[2:7]}-{numero[7:]}"
    print("Numero formatado:" + numero_formatado)
else:
    print("Não é um número válido!")