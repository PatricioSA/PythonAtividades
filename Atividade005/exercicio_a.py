#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio a

import os
os.system('cls')

import math


print('-'*30)
print('CÁLCULO DE RAIZ QUADRADA')
print('-'*30)

#Declaração
resposta = 0

#Entrada de dados
valor = int(input('Digite um valor: '))

#Condicional
if (valor < 0):
    print(f'O resultado será um numero complexo')
elif (valor == 0):
    print(f'Não existe raiz de 0')
    print()
else:

    #Operação
    raizQuadrada = math.sqrt(valor)

    if (raizQuadrada % 2 != 0):
        resposta = math.ceil(raizQuadrada)
    else:
        resposta = raizQuadrada

    #Saída
    print(f'A raiz quadrada de {valor} é: {resposta}')
    print()