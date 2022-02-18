#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/12/2021
#Término: /12/2021


#Limpar o terminal
import os


os.system('cls')

print('='*80)

#declaração
fruta = {}
listaFrutas = []

for c in range(0, 4):
    fruta['Nome'] = str(input('Digite a fruta: '))

    listaFrutas.append(fruta.copy())

print()
for fruta in listaFrutas:
    for chave, valor in fruta.items():
        print(f'{chave} : {valor}')
        
if 'abacaxi' in fruta['Nome']:
    print('Tem abacaxi!')
else:
    print('Que pena, não tem abacaxi')