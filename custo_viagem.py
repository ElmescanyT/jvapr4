dist = int(input('Qual a distância em Km da sua viagem?'))
if dist >= 1 <= 199:
    pqn = dist * 0.50
    print('A sua viagem possui {} Km de distância, sendo assim, o custo total ficou em R${}.'.format(dist, pqn))
elif dist >= 200:
    lgn = dist * 0.45
    print('A sua viagem possui {} Km de distância, sendo assim, o custo total ficou em R${}.'.format(dist, lgn))
