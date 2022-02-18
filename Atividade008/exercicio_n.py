#Autor: Patrício Samuel
#Data início: 26/11/2021
#Término: /11/2021
#Atividade008 - exercicio n
#Faça um programa que sorteia os números da Mega Sena e da Lotofácil

#Limpar o terminal
import os
from random import randint


os.system('cls')

#Título
print('-'*70)
print('Mega Sena - Loterias')
print('='*70)

#Criando a lista
listaMegasena = []

for c in range(0, 6):
    numero = input(f'Aposte o {c+1}º numero: ')
    
    for c in range(0, 10):
        sorteio = randint(1, 20)
    
        if (sorteio not in listaMegasena):
            listaMegasena.append(sorteio)
 
#Saída
print()
print('E os números sorteados foram......')
print(listaMegasena)
print()


#Título
print('-'*70)
print('Lotofácil - Loterias')
print('='*70)

#Criando a lista
listaLotofacil = []

for c in range(0, 25):
    lotofacil = randint(1, 60)
    
    if (lotofacil not in listaLotofacil):
        listaLotofacil.append(lotofacil)

#Saída
print('E os números sorteados foram......')
print(listaLotofacil)
print()