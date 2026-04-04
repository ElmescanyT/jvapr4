print('\033[35mCOMPARAÇÃO ENTRE NÚMEROS!\033[m')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1<n2:
    print('O \033[4;31mmaior\033[m número entre {} e {} é \033[1m{}\033[m.'.format(n1, n2, n2))
elif n1>n2:
    print('O \033[4;31mmaior\033[m número entre {} e {} é \033[1m{}\033[m.'.format(n1, n2, n1))
elif n1 == n2:
    print('\033[4;36mOs dois números são iguais\033[m\033[36m!\033[m')
