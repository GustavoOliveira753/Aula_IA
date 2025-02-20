n1 = float(input("Digite uma nota:"))
n2 = float(input("Digite outra nota:"))
frequencia = float(input("Digite a frequencia:"))
media =(n1+n2)/2

if media >= 6 and frequencia >= 75: 
    print("Aluno aprovado!")
    print("Aproveita as férias!")
elif media >= 2:
    print("O aluno esta de exame!")
    print("Precisa estudar mais um pouco!")
else:
    print("O aluno está reprovado")