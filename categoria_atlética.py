from time import sleep
from datetime import date
hoje = date.today().year
print('-=-' * 30)
print('ATRIBUIÇÃO DE CATEGORIA - CNN - CONFEDERAÇÃO NACIONAL DE NATAÇÃO!')
print('-=-' * 30)
nome = str(input('Qual seu nome?')).capitalize()
nascimento = int(input('Qual o \033[31mANO\033[m de seu nascimento?'))
idade = hoje - nascimento
print('\033[32mO sistema está atribuindo a sua categoria ao banco de dados, aguarde!\033[m')
sleep(3)
print('\033[35mOlá, {}! Segue abaixo sua categoria:\033[m'.format(nome))
sleep(1)
print('\033[34mVocê possui {} anos!\033[m'.format(idade))
sleep(2)
if nascimento >= 2017:
    print('Sua categoria atlética é \033[35mMIRIM!\033[m')
elif nascimento >= 2012:
    print('Sua categoria atlética é \033[34mINFANTIL!\033[m')
elif nascimento >= 2007:
    print('Sua categoria atlética é \033[32mJUNIOR!\033[m')
elif nascimento == 2006:
    print('Sua categoria atlética é \033[33mSÊNIOR!\033[m')
elif nascimento < 2006:
    print('Sua categoria atlética é \033[31mMASTER!\033[m')
print('\033[36m{}, sua categoria atlética foi registrada com sucesso! Aproveite a competição.\033[m'.format(nome, nascimento))
