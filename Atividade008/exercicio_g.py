#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio d
#Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

#Limpar o terminal
import os


os.system('cls')

print('-'*70)
print('')
print('='*70)

#Criando uma lista
listaNúmero = []

for c in range(0, 10):
    numero = int(input(f'Digite o {c+1}º valor: '))
    listaNúmero.append(numero)

maiorValor = max(listaNúmero)
menorValor = min(listaNúmero)

#Sáida
print(f'O maior valor é: {maiorValor}')
print(f'O menor valor é: {menorValor}')