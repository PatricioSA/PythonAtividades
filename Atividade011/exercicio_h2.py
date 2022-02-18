#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 15/02/2022
#Término: 15/02/2022

#Limpar o terminal
import os


os.system('cls')

def media_altura_peso(clientes):
    soma_altura = 0
    soma_peso = 0

    #varrendo os valores para somar a altura e o peso
    #varre a lista
    for registro in clientes:
        #varre o dicionário
        for chave, valor in registro.items():
            if chave == 'altura':
                soma_altura += valor
            if chave == 'peso':
                soma_peso += valor
        print()

    #Calculando a Média
    media_altura = soma_altura/len(clientes)
    media_peso = soma_peso/len(clientes)

    #Saída
    os.system('cls')
    print('PROGRAMA: ACADEMIA')

    print('-'*70)
    print('Código \t\tNome \t\tAltura \t\tPeso')
    print('='*70)

    #varrendo a lista
    for registro in clientes:
        #varrendo o dicionário
        for chave, valor in registro.items():
            #imprime o valor
            print(f'{valor}', end='\t\t')
        print()

    print('-'*70)
    print('Média:', end='\t\t\t\t')
    print(f'{media_altura:.2f}', end='\t\t')
    print(f'{media_peso:.2f}')
    print('='*70)



#Principal
print('PROGRAMA: ACADEMIA')
print('='*70)

cliente = {}
clientes = []

while True:
    cliente['cod'] = int(input('Informe código do cliente: '))
    if cliente['cod'] == 0:
        break
    cliente['nome'] = str(input('Nome do cliente: '))
    cliente['altura'] = float(input('Informe sua altura: '))
    cliente['peso'] = float(input('Informe seu peso: '))
    clientes.append(cliente.copy())

media_altura_peso(clientes)