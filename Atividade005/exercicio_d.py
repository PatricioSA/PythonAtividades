#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio d

#Importando a biblioteca da função
import math
import os


os.system('cls')

#Título
print('-'*40)
print('CÁLCULO DE SENO, COSSENO E TANGENTE')
print('-'*40)

#Entrada de dados
angulo = int(input('Digite o ângulo: '))

#Operações
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#Saída
print(f'O seno do ângulo {angulo}° é: {seno:.2f}')
print(f'O cosseno do ângulo {angulo}° é: {cosseno:.2f}')
print(f'A tangente do ângulo {angulo}° é: {tangente:.2f}')

