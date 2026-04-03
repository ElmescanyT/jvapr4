print('{:=^40}'.format(' LOJINHA ELMESCANY '))
compra = float(input('Qual o valor total da compra?'))
print('''Qual a condição do pagamento?
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
método = int(input('Qual é a opção?'))
if método == 1:
    dsc1 = compra - (compra * 10/100)
    print('Sua compra no valor de R${:.2f} passou para R${:.2f} após um desconto de 10%.'.format(compra, dsc1))
elif método == 2:
    dsc2 = compra - (compra * 5/100)
    print('Sua compra no valor de R${:.2f} passou para R${:.2f} após um desconto de 5%.'.format(compra, dsc2))
elif método == 3:
    print('Sua compra ficou no valor total de R${}.'.format(compra))
elif método == 4:
    parcelas = int(input('Quantas parcelas?'))
    juros = compra + (compra * 20/100)
    total = juros
    parcela = total / parcelas
    print('Sua compra no valor de R${:.2f} passou para R${:.2f} por causa de 20% de Juros.'.format(compra, juros))
    print('R${} parcelado em {}x fica R${:.2f} por mês.'.format(juros, parcelas, parcela))
elif método == 5 or 6 or 7 or 8 or 9 or 10:
    print('\033[31mOpção inválida.\033[m')
