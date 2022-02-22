#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 21/02/2021
#Término: /02/2021
#Atividade012

import os

from operacoes import Operacao


os.system('cls')

operacao1 = Operacao
operacao2 = Operacao

#Entrada de dados
valor1 = int(input('Digite o 1° valor: '))
valor2 = int(input('Digite o 2° valor: '))
valor3 = int(input('Digite o 3° valor: '))

#Operações
resultado1 = operacao1.soma(valor1, valor2, valor3)
resultado2 = operacao2.produto(valor1, valor2, valor3)

#Saída
print('='*50)
print(f'A soma dos valores é: {resultado1}')
print(f'A multiplicação dos valores é: {resultado2}')
print('='*50)