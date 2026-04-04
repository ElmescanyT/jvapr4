soma = 0
contador = 0
for numero in range(1, 501):
    if numero % 3 == 0:
        soma += numero
        contador += 1
print("A soma dos {} valores solicitados é: {}".format(contador, soma))