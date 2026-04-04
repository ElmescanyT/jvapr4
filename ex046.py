from time import sleep
print('A contagem regressiva para o estouro vai começar!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mBOOM!!!\033[m')