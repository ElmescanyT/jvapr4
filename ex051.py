from time import sleep
pt = int(input('Qual o primeiro termo da PA?'))
rz = int(input('Qual a razão da PA?'))
print('Os \033[31mDEZ\033[m primeiros termos dessa PA é:')
for c in range(1, 11):
    clc = pt + (c - 1) * rz
    sleep(0.5)
    print('{}'.format(clc))