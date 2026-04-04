from time import sleep
from datetime import date
hoje = date.today().year
print('-=-' * 20)
print('\033[32mVERIFICAÇÃO DE ALISTAMENTO MILITAR BRASILEIRO!\033[m')
print('-=-' * 20)
nome = str(input('Qual seu nome?'))
gnr = str(input('Qual seu sexo? (Masculino ou Feminino)')).strip().capitalize()
nascimento = int(input('Qual o ano do seu nascimento?'))
print('Olá, {}! \033[33mAguarde enquanto o sistema verifica sua situação militar!\033[m'.format(nome))
sleep(4)
idade = hoje - nascimento
if  gnr == 'Feminino':
    print('Você não precisa se alistar por ser mulher!')
if gnr == 'Masculino' and nascimento == 2008 or idade == 18:
    print('\033[33mVocê possui 18 anos, está na hora de se alistar!\033[m')
elif gnr == 'Masculino' and nascimento > 2008 or idade < 18:
    saldo = 18 - idade
    print('\033[32mVocê possui menos de 18 anos, portanto, ainda não está na hora de se alistar.\033[m')
    print('Ainda faltam {} anos para o seu alistamento militar.'.format(saldo))
    ano = hoje + saldo
    print('Seu alistamento militar será em {}.'.format(ano))
elif gnr == 'Masculino' and nascimento < 2008 or idade > 18:
    print('\033[31mVocê possui mais de 18 anos, portanto, deve se alistar imediatamente.\033[m')
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = hoje - saldo
    print('Seu alistamento foi em {}.'.format(ano))