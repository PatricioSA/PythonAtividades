#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('Lista')
print('='*80)

#Função
def lista_numeros():
    listaNumeros = []
    listaPares = []
    listaImpares = []
    for c in range(0, 8):
        numero = int(input(f'Digite o {c+1}º numero: '))
        listaNumeros.append(numero)
        if numero % 2 == 0:
            listaPares.append(numero)
            quantidadePares = len(listaPares)
        else:
            listaImpares.append(numero)
            quantidadeImpares = len(listaImpares)
    
    print(f'A lista é {listaNumeros}')
    print(f'Os pares são{listaPares}')
    print(f'{quantidadePares} números pares')
    print(f'Os impares são{listaImpares}')
    print(f'{quantidadeImpares} numeros impares')

lista_numeros()