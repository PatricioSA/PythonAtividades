#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: /11/2021
#Término: /11/2021
#Atividade005 - Exercício g

from math import pow, sqrt

import os
os.system('cls')


print('-'*50)
print('CÁLCULO DE EQUAÇÃO')
print('-'*50)

#Entrada de dados
a = int(input('informe o valor de "a" '))
b = int(input('informe o valor de "b" '))
c = int(input('informe o valor de "c" '))

#Operações
xUm = ((-b) + (sqrt((pow(b, 2) - 4 * a * c)))) / 2 * a
xDois = ((-b) - (sqrt((pow(b, 2) - 4 * a * c)))) / 2 * a

#Saída
print('-'*50)
print(f'Resolvendo a equação ....')
print(f'O resultado é: {xUm} e {xDois}')

print()
print('Fim do Programa! ')