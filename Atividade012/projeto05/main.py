#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 21/02/2021
#Término: 11/02/2021
#Atividade012

import os

from triangulo import Triangulo


os.system('cls')

#instanciado
triangulo = Triangulo
triangulo2 = Triangulo

#entrada de dados
ladoUm = int(input('Digite o valor do 1º segmento: '))
ladoDois = int(input('Digite o valor do 2º segmento: '))
ladoTres = int(input('Digite o valor do 3º segmento: '))

#condição existencia
resultado1 = triangulo.condicao_existencia(ladoUm, ladoDois, ladoTres)

#perímetro
resultado2 = triangulo.perimetro(ladoUm, ladoDois, ladoTres)

#Saída
os.system('cls')
print('-'*60)
print(f'Os segmentos {ladoUm}, {ladoDois}, {ladoTres} {resultado1}')
print(f'O perímetro é {resultado2}')