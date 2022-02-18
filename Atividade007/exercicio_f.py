#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: /11/2021
#Atividade007 - exercício c

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('')
print('='*50)

print()

for c in range(1, 100):
    divisores = 0
    
    for j in range(1, c + 1):
        if (c % j == 0):
            divisores += 1
    
    if (divisores == 2):
        print(c, end= ' ')

print()
print('='*70)
