#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 04/11/2021
#Término: 04/11/2021
#Atividade004 - Exercício c

#Limpando terminal
import os
os.system('cls')

#Entrada de dados
velocidade = int(input('Digite a velocidade do carro em km/h: '))

#Condicionais
if (velocidade < 0):
    print('Velocidade inválida')
elif (velocidade > 60):
    print('Velocidade acima do permitido! ')
else:
    print('Velocidade normal! ')