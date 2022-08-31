"""
Entrada de dados
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

ano_nascimento = 2022 - int(idade)
print(f'{nome} nasceu em {ano_nascimento}, então tem {idade} anos.')

