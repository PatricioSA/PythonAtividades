#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 21/02/2021
#Término: /02/2021
#Atividade012

import os

from salario import Salario

os.system('cls')

print('-'*30)
print('CÁLCULO DE AUMENTO DE SALÁRIO ')
print('-'*30)

#
salario1 = Salario

#Entrada de dados
valor = float(input('Digite o salário: '))

salario1.aumento(valor)

print(salario1)