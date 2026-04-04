from time import sleep
from datetime import date
maioridade = 0
menoridade = 0
atual = date.today().year
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('\033[33mAnalisando dados...\033[m')
sleep(2)
print('\033[31m{} pessoas são maiores de idade!\033[m\n\033[32m{} pessoas são menores de idade!\033[m'.format(maioridade, menoridade))
