#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: 26/11/2021
#Listas

#Limpar o terminal
import os


os.system('cls')

print('-'*70)
print('')
print('='*70)

#Criando uma lista
listaNumeros = []
soma = 0

for c in range(0, 5):
    numero = int(input(f'Entre com o {c+1}º: '))

    #Guardando em uma lista
    listaNumeros.append(numero)
    soma += numero

print()
print(listaNumeros)
print(soma)