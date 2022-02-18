#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/10/2021
#Término: 09/10/2021
#Atividade005 - exercicio f

#Importando a biblioteca da função
from random import randint
import os


os.system('cls')

#Título
print('-'*30)
print('EM QUE NÚMERO ESTOU PENSANDO?')
print('-'*30)

#Entrada de dados e Declaração
numero = int(input('Digite um número de 1 a 5: '))
aleatorio = randint(1, 5)

#Saída
if (numero < 1 or numero > 5):
    print('Número Inválido. O número deve ser entre 1 e 5')
elif (numero == aleatorio):
    print(f'Parabéns você acertou! o número era {aleatorio} ')
else:
    print(f'Você errou, o número era {aleatorio}')