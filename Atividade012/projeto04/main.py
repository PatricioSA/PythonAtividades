#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 21/02/2021
#Término: /02/2021
#Atividade012

import os

from salario import Funcionario


os.system('cls')

print('-'*30)
print('CÁLCULO DE AUMENTO DE SALÁRIO ')
print('-'*30)

#instanciando
pedro = Funcionario('Pedro Alves', 42, 900)

#Saída
print(f'Nome: {pedro.nome}')
print(f'Idade: {pedro.idade}')
print(f'Salário: {pedro.salario}')
print('-'*30)
print(f'Salário Novo:') 
pedro.aumento(900)