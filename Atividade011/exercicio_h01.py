#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/02/2022
#Término: /02/2022

from time import sleep
import os


os.system('cls')


def media(listaClientes):
    somaAltura = 0
    somaPeso = 0

    #varrendo os valores para somar a altura e o peso
    #varre a lista
    for registro in clientes:
        #varre o dicionário
        for chave, valor in registro.items():
            if chave == 'Altura':
                somaAltura += valor
            if chave == 'Peso':
                somaPeso += valor
        print()

    #Calculando a Média
    mediaAltura = somaAltura/len(clientes)
    mediaPeso = somaPeso/len(clientes)

    #Saída lista de clientes
    print('CADASTRO DE CLIENTES')
    print('-'*70)
    print('Código \t\tNome \t\tAltura \t\tPeso')
    print('='*70)
    for registro in (listaClientes):
        print()
        for valor in registro.items():
            print(f'{valor}', end=' \t\t')
    print()
    print('-'*70)
    print(f'Média:                          {mediaAltura:.2f}            {mediaPeso}')
    print('='*70)


listaClientes = []
cliente = {}

while (True):
    
    #Entrada de dados
    cliente['Código'] = (input('Entre com o código: '))
    if not(cliente['Código'].isnumeric()):
        print('Inválido')
        continue
    else:
        cliente['Código'] = int(cliente['Código'])
    
    while (True):
        cliente['Nome'] = (input('Entre com seu nome: ')).capitalize()
        if (cliente['Nome'].isnumeric()):
            print('Inválido')
        else:
            cliente['Nome'] = str(cliente['Nome'])
            break
    
    cliente['Altura'] = float(input('Altura: '))
    cliente['Peso'] = float(input('Peso: '))
        
    #copiando dicionário para dentro da lista
    listaClientes.append(cliente.copy())

    #
    print()
    pergunta = str(input('Deseja cadastrar mais clientes? (s/n): '))
    if pergunta != 's' and pergunta != 'n':
        print('Inválido')
    elif pergunta == 's':
        os.system('cls')
        print('-'*80)
        print('Cadastro de clientes da Academia')
        print('='*80)
        continue
    else:
        break

media(listaClientes)

