#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 06/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

print('='*80)

#Função que coloca duas listas dentro do dicionário
def converter_listas(lista1, lista2):
    
    listaNova = dict(zip(lista1, lista2))
    return listaNova

#Declaração
lista1 = ['Nome', 'Peso', 'Idade']
lista2 = []

#Entrada de dados
nome = str(input('Digite um nome: ')).capitalize()
peso = float(input('Digite o peso: '))
idade = int(input('Digite a idade: '))

#Adicionando os dados na lista
lista2.append(nome)
lista2.append(peso)
lista2.append(idade)

#invacando a função
retorno = converter_listas(lista1, lista2)

#limpar tela
os.system('cls')

#Saída
print(f'A lista 1 é: {lista1}')
print('-'*40)
print(f'A lista dois é: {lista2}')
print('-'*40)

for chave, valor in retorno.items():
    print(f'{chave}: {valor}', end='\t')
print()