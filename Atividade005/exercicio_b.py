#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio b

#Importando a biblioteca da função
import math
import os


os.system('cls')

#Entrada de dados
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))

#Operações
divisao = valor1 / valor2
arredondarCima = math.ceil(divisao)
arredondarBaixo = math.floor(divisao)

#Condicionais
if (valor2 == 0):
    print('Não existe divisão por zero')
elif (divisao % 2 == 0):
    print(f'O resultado da divisão é: {divisao}')
else:
    print(f'A divisão arredondada para baixo é {arredondarBaixo}')
    print(f'A divisão arredondada para cima é {arredondarCima}')
