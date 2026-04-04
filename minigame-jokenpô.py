from random import choice
from time import sleep
print('-=-=' * 10)
print('MINIGAME - JOKENPÔ!')
print('\033[31mTente ganhar de mim!\033[m')
print('-=-=' * 10)
usuário = str(input('Pedra, Papel ou Tesoura?')).strip().capitalize()
possibilidades = ['Pedra', 'Papel', 'Tesoura']
embaralho = choice(possibilidades)
print('\033[33mJO\033[m')
sleep(1)
print('\033[32mKEN\033[m')
sleep(1)
print('\033[34mPÔ!!!\033[m')
if embaralho == 'Tesoura' and usuário == 'Papel':
    print('Eu escolhi {} e você escolheu {}. \033[31mEu ganhei de você!\033[m'.format(embaralho, usuário))
elif embaralho == 'Pedra' and usuário == 'Tesoura':
    print('Eu escolhi {} e você escolheu {}. \033[31mEu ganhei de você!\033[m'.format(embaralho, usuário))
elif embaralho == 'Papel' and usuário == 'Pedra':
    print('Eu escolhi {} e você escolheu {}. \033[31mEu ganhei de você!\033[m'.format(embaralho, usuário))
elif usuário == 'Pedra' and embaralho == 'Tesoura':
    print('Eu escolhi {} e você escolheu {}. \033[32mVocê ganhou de mim!\033[m'.format(embaralho, usuário))
elif usuário == 'Papel' and embaralho == 'Pedra':
    print('Eu escolhi {} e você escolheu {}. \033[32mVocê ganhou de mim!\033[m'.format(embaralho, usuário))
elif usuário == 'Tesoura' and embaralho == 'Papel':
    print('Eu escolhi {} e você escolheu {}. \033[32mVocê ganhou de mim!\033[m'.format(embaralho, usuário))
elif embaralho == usuário:
    print('Eu escolhi {} e você escolheu {}. \033[37mEMPATE!\033[m \033[32mTente novamente.\033[m'.format(embaralho, usuário))
else:
    print('\033[32mNão consegui identificar sua resposta. Tente novamente!\033[m')
