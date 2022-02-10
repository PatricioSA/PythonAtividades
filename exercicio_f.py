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
lista2 = ['John', 40, 1.8]

#invacando a função
retorno = converter_listas(lista1, lista2)

#Saída
print(f'A lista 1 é: {lista1}')
print(f'A lista dois é: {lista2}')
print(f'A lista convertida é: {retorno}')