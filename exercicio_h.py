#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 09/02/2022
#Término: /02/2022

#Limpar o terminal
import os


os.system('cls')

#Título
print('-'*80)
print('Cadastro de clientes da Academia')
print('='*80)

#Declarações
listaClientes = []
cliente = {}
somaAltura = 0
somaPeso = 0
mediaAltura = 0
mediaPeso = 0
quantidade = 0

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

    #Cálculos de média
    quantidade += 1
    somaAltura += cliente['Altura']
    somaPeso += cliente['Peso']
    mediaAltura = somaAltura / quantidade
    mediaPeso = somaPeso / quantidade
        
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

os.system('cls')

#Saída lista de clientes
print('CADASTRO DE CLIENTES')
print('-'*70)
print('Código \t\tNome \t\tAltura \t\tPeso')
print('='*70)
for i, c in enumerate(listaClientes):
    print()
    for valor in c.values():
        print(f'{valor}', end=' \t\t')
print()
print('-'*70)
print(f'Média:                          {mediaAltura:.2f}            {mediaPeso}')
print('='*70)