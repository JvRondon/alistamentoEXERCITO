from datetime import date
atual = date.today().year
anoNascimento = int(input("Ano do seu nascimento: "))
idade = atual - anoNascimento
print("Você nasceu em {}, tem {} anos em {}.".format(anoNascimento, idade, atual))

if(idade == 18):
    print("Você precisa se alitar IMEDIATAMENTE!")
elif(idade < 18):
    saldo=18 - idade
    ano = atual + saldo
    print("Ainda faltam {} anos para você se alistar!".format(saldo))
    print("Seu alistamento será realizado em {}.".format(ano))
elif(idade > 18):
    saldo=idade - 18
    ano = atual - saldo
    print("Você deveria ter se alistado há {} anos!".format(saldo))
    print("Seu alistamento foi em {}.".format(ano))