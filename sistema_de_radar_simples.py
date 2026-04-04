carro = int(input('Qual a velocidade do carro?'))
print('A velocidade do seu veículo foi \033[33m{} Km/h.\033[m'.format(carro))
if carro >= 80:
    multa = (carro-80) * 12
    print('\033[31mO limite máximo foi excedido! O limite é 80Km/h.\033[m')
    print('Você irá ser multado(a) no valor de \033[33mR${:.2f} reais.\033[m'.format(multa))
else:
    print('\033[32mVocê está dentro da velocidade permitida!\033[m')
print('Tenha um bom dia! \033[4mDirija com segurança\033[m!')
