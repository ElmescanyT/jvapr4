# For precisa ter um número limite, já o while not não
# while not = enquanto não
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''
'''for c in range(1, 5):
    n = int(input('DIGITE UM NÚMERO:'))'''
'''n = 1
while n !=0:
    n = int(input('Digite um número: '))
print('Fim!')'''
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper() # Enquanto for a variável R receber S, vai continuar o laço
print('Fim!')'''
n = 1
par = 0
impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
                par += 1
        else:
            impar += 1
print('Você digitou {} números pares.\nVocê digitou {} números ímpares.'.format(par, impar))