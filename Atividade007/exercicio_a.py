#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 18/11/2021
#Término: 18/11/2021
#Atividade007 - exercício a

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*50)
print('IMPRIME DE 1 A 100')
print('='*50)

print()

#Estrutura de repetição
for c in range(0, 100):
    print(c + 1, end=' ')


#Utilizando o While

#Declaração
contador = 0

#Repetição
while (contador <= 100):
    contador += 1
    print(contador, end=' ')
