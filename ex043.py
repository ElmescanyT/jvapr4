altura = float(input('Qual sua altura?'))
peso = float(input('Qual seu peso?'))
imc = peso/(altura * altura)
print('Seu IMC é {}.'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso.')
elif 18.6 <= imc <= 25:
    print('Peso ideal.')
elif 25.1 <= imc <= 30:
    print('Sobrepeso.')
elif 30.1 <= imc <= 35:
    print('Obesidade grau I.')
elif 35.1 <= imc <= 40:
    print('Obesidade grau II (Severa).')
elif imc >= 40.1:
    print('Obesidade mórbida.')
