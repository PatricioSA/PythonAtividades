#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 05/11/2021
#Término: 05/11/2021
#Atividade004 - Exercício f

#Limpando terminal
import os
os.system('cls')

#Entrada de dados
a = int(input('informe o valor de "a" '))
b = int(input('informe o valor de "b" '))
c = int(input('informe o valor de "c" '))

#Operações
# x = (-b ± √∆) / 2 * a
delta = b ** 2 - 4 * a * c
xUm = (- b + delta ** (1/2)) / 2 * a
xDois = (- b - delta ** (1/2)) / 2 * a

#Saída
print('-'*50)
print('CÁLCULO DE EQUAÇÃO')
print('-'*50)
print(f'resolvendo a equação ....')
print(f'O resultado é: {xUm} e {xDois}')

print()
print('Fim do Programa! ')