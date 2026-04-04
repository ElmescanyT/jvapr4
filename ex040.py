from time import sleep
n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
média = (n1 + n2)/2
print('A sua média foi {:.2f}!'.format(média))
print('\033[33mO sistema está verificando sua situação acadêmica...\033[m')
sleep(3)
if média < 5:
    print('Você está \033[31mREPROVADO!\033[m')
elif 5 <= média <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO!\033[m Procure o docente responsável pela matéria.')
elif média >= 7:
    print('Você está \033[32mAPROVADO!\033[m Parabéns pela aprovação!')