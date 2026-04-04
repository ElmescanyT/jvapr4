soma_idade = 0
maior_idade_homem = 0
mulheres = 0
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    nome = str(input('Qual seu nome?')).strip()
    idade = int(input('Qual sua idade?'))
    print('''Selecione o seu SEXO:
[ 1 ] Homem
[ 2 ] Mulher''')
    sexo = int(input('Qual sua opção?'))
    soma_idade += idade
    if sexo == 1 and idade > maior_idade_homem:
        maior_idade_homem = idade
        velho = nome
    if sexo == 2 and mulheres < 20:
        mulheres += 1
media = soma_idade / 4
print('A média de idade do grupo é: {} anos.'.format(media))
print('{} mulheres possuem menos de 20 anos.'.format(mulheres))
print('O homem mais velho do grupo possui {} anos e ele se chama {}.'.format(maior_idade_homem, velho))
