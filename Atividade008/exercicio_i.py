#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio d
#Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

#Limpar o terminal
import os


os.system('cls')

#Criando as listas
listaNumeros = []

while (True):
    print('')
    print('='*70)

    #Entrada de dados
    numero = input('Digite um número [s ou - sair]: ').lower()
    
    if(numero == 's'):               
        break
    
    # Validação
    else:
        if ((not(numero.isnumeric()))):
            print()
            print(f'Entrada Inválida, digite novamente...')
            print()
        else:
            numero = int(numero)
            listaNumeros.append(numero)

listaFatida = listaNumeros[0:10]
listaFatida2 = listaNumeros[10:20]
listaFatida3 = listaNumeros[20:30]
listaFatida4 = listaNumeros[30:40]
listaFatida5 = listaNumeros[40:50]

#Saída
print(f'Lista 1: {listaFatida}')
print(f'Lista 2: {listaFatida2}')
print(f'Lista 3: {listaFatida3}')
print(f'Lista 4: {listaFatida4}')
print(f'Lista 5: {listaFatida5}')