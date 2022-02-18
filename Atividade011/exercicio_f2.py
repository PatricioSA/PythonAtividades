#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 14/02/2021
#Término: 14/02/2021

#Limpar o terminal
import os


os.system('cls')

def monta_dicionario(lista1, lista2):
    #uso da função zip()
    #esta função faz a junção das listas:
    #a 1ª lista se torna chave e a segunda o valor
    dicionario = dict(zip(lista1, lista2))

    return dicionario

#principal
lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['John', 40, 1.80]

print('-'*70)
print('Juntando listas em dicionário')
print('='*70)

print(f'Listas 1:', end=' ')
for item in lista_1:
    print(f'{item}', end='\t')

print()
print(f'Lista 2:', end=' ')
for item in lista_2:
    print(f'{item}', end='\t')
print()
print('-'*70)

print()
print('Dicionário Montado com lista 1 e 2')
print('='*70)

resultado = monta_dicionario(lista_1, lista_2)

for chave, valor in resultado.items():
    print(f'{chave}: {valor}', end='\t')
print()
print('-'*70)
print()