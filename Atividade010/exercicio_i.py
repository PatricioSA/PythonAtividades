#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 07/12/2021
#Término: /12/2021
#Faça um programa para criar um dicionário com 4 elementos. Depois imprima a lista completa, 
# delete o ultimo elemento e mostre uma listagem nova com esse elemento excluído.

#Limpar o terminal
import os


os.system('cls')

print('='*80)

#declaração
carro = {}

#Entrada de dados
carro['Nome'] = str(input('Digite o nome do carro: '))
carro['Marca'] = str(input('Digite a marca: '))
carro['Potência'] = str (input('Digite a quantidade de cavalos: '))
carro['Ano'] = int(input('Digite o ano de fabricação: '))

os.system('cls')

#Imprimindo o dicionário
for chave, valor in carro.items():
    print(f'{chave} : {valor}')
print()

#Excluindo o último elemento
carroAtualizado = carro.popitem()

#Saída final
print(carro)
print(f'Elemento excluido {carroAtualizado}')