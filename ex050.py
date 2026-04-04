soma = 0
cont = 0
for p in range(1, 7):
    n = int(input('Digite o {} número: '.format(p)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma entre {} número(s) pares foi {}.'.format(cont, soma))