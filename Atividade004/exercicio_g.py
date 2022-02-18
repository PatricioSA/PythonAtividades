#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 05/11/2021
#Término: 05/11/2021
#Atividade004 - Exercício g

#Limpando terminal
import os
os.system('cls')

print('-'*40)
print('CÁLCULO DA CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO ')
print('-'*40)


#Entrada de dados
ladoUm = int(input('Digite o valor do 1º segmento: '))
ladoDois = int(input('Digite o valor do 2º segmento: '))
ladoTres = int(input('Digite o valor do 3º segmento: '))

#Condicionais
if (ladoUm <= 0) or (ladoDois <= 0) or (ladoTres <= 0):
    print('Valores Inválido')
elif (ladoUm + ladoDois > ladoTres) and (ladoUm + ladoTres > ladoDois) \
    and (ladoDois + ladoTres > ladoUm):
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')

print()
print('Fim do programa')