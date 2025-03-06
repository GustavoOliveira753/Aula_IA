data = input("Data de nascimento: ")
meses = {'1': "Janeiro", '2': "Fevereiro", '3': "Março", '4': "Abril", '5': "Maio", '6': "Junho", '7': "Julho", '8': "Agosto", '9': "Setembro", '10': "Outubro", '11': "Novembro", '12': "Dezembro"}
dia, mes, ano = data.split("/")

print(f"Você nasceu em {dia} de {meses.get(mes, 'Mes inválido')} de {ano}")