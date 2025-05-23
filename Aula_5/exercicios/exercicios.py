import funcoes

nomes = "ANA CLARA NOGUEIRA DE ARAÚJO;ANA LAURA FARIA SANTOS;ANA LAURA FERNANDES DA SILVA;BETÂNIA AMÂNCIO PEREIRA;BRENO ESTORARI DA SILVA;EDUARDO BELLO GALEGO;EDUARDO HENRIQUE DO CARMO;ERIKA DE BRITTO CÔNSOLO;FERNANDA GARCIA FLORIANO;GIUSEPPE FRANCESCO STRACERI IANES BAGGIO;GUSTAVO MEDEIROS DE BARROS;GUSTAVO PEREIRA GARCIA;JOAO PEDRO BILLO LUCIANO;JOAO VICTOR SALOTI ALVES;KAUA DANTAS MARTINS;KEVIN RENAN NOGUEIRA DA SILVEIRA;LAIS CUNHA THEODORO DA SILVA;LAVINIA DAL BELLO E SOUZA;LUIS OTAVIO FLORENCIO BARBOSA;LUIS OTAVIO MORAIS DE SOUZA;LUIZA HELENA TARDELLI MARCULLI ESPINDOLA;MARIA CAROLINA SILVA GARCIA;MARIA CLARA SANTOS MANETA;MARIA FERNANDA GRESPAN BENFEITO;MARIA FERNANDA TOBIAS CHAGAS;MATHEUS CARVALHO FELISBERTO;MURILO ANTONIO BARION;NICOLY GOMES SERRANO;OCTAVIO AUGUSTO ANDREAZZI CHAVES;PEDRO VINICIUS VIEIRA VASCONCELLOS;RAFAEL CREMASCO;RAFAEL LOPES PIRES;RAQUEL MOREIRA FERNANDES CUSTODIO;RENAN HENRIQUE TEIXEIRA;SABRYNA SATORRES BATISTINI;SOPHIA RUEDA GONÇALVES DA RITA;TAYNARA DE MELLO SIQUEIRA;TIFANI SCHIAVON MISSURA;VITORIA CIPRIANO DE JESUS;WESLEY RICARDO SILVA PEREIRA"

notas = "9.33;8.76;6.11;1.09;2.76;2.97;9.04;3.62;3.37;1.76;8.14;2.48;3.27;9.16;9.01;1.55;2.98;3.41;8.45;5.79;0.54;2.01;6.78;1.09;4.75;0.09;7.62;0.53;8.95;6.93;1.04;2.87;7.85;6.65;6.96;9.72;9.42;0.44;6.78;7.54"

faltas = "23;5;14;5;29;20;19;2;23;5;18;27;6;8;28;29;5;7;7;19;6;14;4;21;25;25;17;23;21;13;1;19;27;21;26;27;7;19;5;21"

nomesArr, notasArr, faltasArr = funcoes.stringToList(nomes, notas, faltas)

count = 0

print("Lista dos alunos:\n")
for i in range(40):
    print(f"Nome: {nomesArr[i]}\nNota: {notasArr[i]}\nFalta: {faltasArr[i]}\n")
print("Lista dos alunos aprovados:\n")
for i in range(40):
    if float(notasArr[i])>=6.0:
        print(f"Nome: {nomesArr[i]}\nNota: {notasArr[i]}\nFalta: {faltasArr[i]}\n")
        count+=1
print(f"Quantidade de alunos aprovados: {count}\n")
count = 0
print("Alunos reprovados por frequência:\n")
for i in range(40):
    if int(faltasArr[i])>20:
        print(f"Nome: {nomesArr[i]}\nNota: {notasArr[i]}\nFalta: {faltasArr[i]}\n")
        count+=1
print(f"Quantidade de alunos reprovados por frequência: {count}\n")
count = 0
print("Listagem dos alunos que possuem o sobrenome SILVA:\n")
for i, nome in enumerate(nomesArr):
    if "SILVA" in nome.upper():
        print(f"Nome: {nomesArr[i]}\nNota: {notasArr[i]}\nFalta: {faltasArr[i]}\n")
        count+=1
print(f"Quantidade de alunos com o sobrenome SILVA: {count}\n")
count = 0
print("Nomes e sobrenomes:")
nomesFormat = (f'{nome.split()[0].capitalize()} {nome.split()[-1].capitalize()}' for nome in nomesArr)
for nome in nomesFormat:
    print(nome)
nomesAbreviados = (f"{partes[0].capitalize()} " + ''.join([f"{p[0].capitalize()}. " for p in partes[1:-1]]) + f" {partes[-1].capitalize()}"for nome in nomesArr for partes in [nome.split()])
for nomes in nomesAbreviados:
    print(nomes)