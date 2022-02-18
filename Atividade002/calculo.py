#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 27/10/2021
#Término: 28/10/2021
#Atividade 002

#entrada
a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))

#operações
#soma
soma = a + b
#subtração
subtracao = a - b
#produto
produto = a * b
#divisão
divisao = a / b
#Potência
potencia = a ** b
#Divisão Inteira
divisaoInteira = a // b
#Resto da divisão
restoDivisao = a % b
#Raiz quadrada
raizQuadrada = a ** (1/2)
#Raiz Cúbica
raizCubica = a ** (1/3)

#Saída
print('='*40)
print('ESTUDO DE OPERADORES ARITMÉTICOS')
print(f'O valor de {a} + {b} = {soma}')
print(f'O valor de {a} - {b} = {subtracao}')
print(f'O valor de {a} x {b} = {produto}')
print(f'O valor de {a} / {b} = {divisao:.2f}')
print(f'O valor de {a} ** {b} = {potencia}')
print(f'O valor de {a} // {b} = {divisaoInteira}')
print(f'O valor de {a} % {b} = {restoDivisao}')
print(f'A raiz quadrada de {a} é: {raizQuadrada:.2f}')
print(f'A raiz cúbica de {a} é: {raizCubica:.2f}')
print(f'='*40)