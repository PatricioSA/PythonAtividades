#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio k
#

#Limpar o terminal
import os


os.system('cls')

#Criando listas
listaNumeros = []
listaPar = []
listaImpar = []

for c in range(0, 7):

    #Entrada de dados
    numero = int(input('Digite um numero: '))
    listaNumeros.append(numero)

    if (numero % 2 == 0):
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

#Saída
print(f'A lista é: {listaNumeros}')
print(f'A lista par é: {listaPar}')
print(f'A lista impar é: {listaImpar}')


