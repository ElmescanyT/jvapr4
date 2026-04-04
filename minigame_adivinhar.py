from random import randint
from time import sleep # Faz o computador dormir
print('-=-' * 20)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar!')
print('-=-' * 20)
nmr = int(input('Pense no número que eu escolhi:'))
print('\033m[32mPROCESSANDO...\033[m')
sleep(3)
pensar = randint(0,5)
print('O número escolhido foi {}.'.format(pensar))
if nmr == pensar:
   print('Você acertou o número. PARÁBENS!')
else:
    print('Você errou! Tente novamente.')
