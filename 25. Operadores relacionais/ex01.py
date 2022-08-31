"""
Operadores relacionais
== Igual
> Maior que
>= Maior que ou igual a
< Menor que
<= Menor ou igual que
!= Diferente
"""
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

ig = (num1 == num2)
men = (num1 < num2)

print(f'O número {num1} é igual ao número {num2}? {ig}')
print(f'O número {num1} é menor ao número {num2}? {men}')