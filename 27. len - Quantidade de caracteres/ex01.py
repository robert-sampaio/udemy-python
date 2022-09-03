usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Número de caracteres insuficiente. Digite no mínimo 6 caracteres.")
else:
    print("Você foi cadastrado no sistema.")