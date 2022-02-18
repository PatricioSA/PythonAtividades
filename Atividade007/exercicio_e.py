#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: /11/2021
#Atividade007 - exercício e

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

print()

#Declaração
soma = 0
quantidadePares = 0

#Estrutura de repetição
for c in range(0, 100 + 1):

    if (c % 2 == 0):
        print(c, end=' ')

        soma += c

        quantidadePares += 1

print()
print(f'A soma dos pares dos números de 0 a 100 é: {soma}')
print(f'A quantidade de pares de 0 a 100 é: {quantidadePares}')
print()