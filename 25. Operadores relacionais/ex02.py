nome = input('Qual o seu nome? ')
id = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
id_menor = 18   # muito jovem
id_maior = 25   # passou da idade

if id < id_menor:
    print(f'{nome} NÃO pode pegar o empréstimo pois é muito novo.')
elif id > id_maior:
    print(f'{nome} NÃO pode pegar o empréstimo pois é muito velho.')
else:
    print(f'{nome} pode pegar o empréstimo.')

