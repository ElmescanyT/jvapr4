n = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(n))
for i in range(1, 11):
    print('{} x {} = {}.'.format(n, i, n*i))
