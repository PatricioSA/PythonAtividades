#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio c
# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares• Os números ímpares• Os múltiplos de 2, 3 e 4
# • Lista reversa• O produto dos intervalos 5-6 por 11-12

#Limpar o terminal
import os


os.system('cls')

print('-'*70)
print('')
print('='*70)

#Criando uma lista
listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

fatiamento1 = listaNumeros[0:9]
fatiamento2 = listaNumeros[7:13]
fatiamento3 = listaNumeros[1:15:2]
fatiamento4 = listaNumeros[0:15:2]
multiplos2 = listaNumeros[1:15:2]
multiplos3 = listaNumeros[2:15:3]
multiplos4 = listaNumeros[3:15:4]
produto = listaNumeros[5]*listaNumeros[11], listaNumeros[6]+listaNumeros[12]
listaNumeros.reverse()



#Saída
print(f'Intervalo de 1 a 9: {fatiamento1}')
print(f'Intervalo de 8 a 13: {fatiamento2}')
print(f'Números pares: {fatiamento3}')
print(f'Números ímpares: {fatiamento4}')
print(f'múltiplos de 2: {multiplos2}')
print(f'múltiplos de 3: {multiplos3}')
print(f'múltiplos de 4: {multiplos4}')
print(f'Lista reversa: {listaNumeros}')
print(produto)
print()