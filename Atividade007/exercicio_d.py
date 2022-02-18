#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: 18/11/2021
#Atividade007 - exercício c

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

print()

#Estrutura de repetição
for c in range(0, 100):

    if (c % 2 == 0):
        print(c, end=' ')

#Exemplo com while
print('For range, números pares [0-100]')
print('-'*70)

contador = -2
while (contador <= 98):
    contador += 2
    print(f'{contador}', end=' ')