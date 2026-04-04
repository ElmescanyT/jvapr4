a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}.\033[m'.format(a, b)) # Sempre lembrar de cessar a cor terminando com \033[m
# Utilizando format:
cores = {'final':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'} # Dicionário
print('{}{}{}'.format(cores['azul'], a, cores['final'])) # Utilizar '' quando usar cor no format.
