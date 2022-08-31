usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'SlyShieda'
senha_bd = '51773933'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')