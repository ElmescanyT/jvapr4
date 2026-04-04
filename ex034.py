slr = float(input('Qual o seu salário?'))
if slr >= 1250.00:
    aumntsup = slr * 1.10
    print('O seu salário atual é de R${:.2f} e passará a ser R${:.2f} após aumento de 10%.'.format(slr, aumntsup))
else:
    aumentinf = slr * 1.15
    print('O seu salário atual é de R${:.2f} e passará a ser R${:.2f} após aumento de 15%.'.format(slr, aumentinf))
