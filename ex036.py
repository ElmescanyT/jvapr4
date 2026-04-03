from time import sleep
print('-=-' * 20)
print('\033[35mSISTEMA DE EMPRÉSTIMO BANCÁRIO!\033[m')
print('-=-' * 20)
casa = float(input('Qual o valor do imóvel que você deseja financiar? R$'))
salário = float(input('Qual o seu salário mensal? R$'))
tempo = int(input('Você deseja financiar em quantos anos? '))
prest = casa / (tempo * 12)
limite = salário * 0.30
print('Você deseja financiar um imóvel no valor de R${} reais em {} anos. A prestação mensal será de R${:.2f} reais.'.format(casa, tempo, prest))
print('\033[33mCONSULTANDO AUTORIZAÇÃO...\033[m')
sleep(4)
if prest <= limite:
    print('\033[32mSeu empréstimo no valor de R${} reais foi autorizado pela\033[m \033[4;34mCaixa Econômica Federal\033[m\033[34m.\033[m'.format(casa))
else:
    print('\033[31mSeu empréstimo foi negado porque sua remunaração mensal excedeu o limite de 30% nas prestações mensais.\033[m')
