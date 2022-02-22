import os

from ano import Pessoa

from datetime import date


os.system('cls')

while(True):
    #Entrada de dados
    nome = str(input('Digite o nome: ')).capitalize()
    nascimeto = int(input('Digite seu ano de nascimento: '))

    #instanciando
    pessoa1 = Pessoa(nome, nascimeto)

    #pegando o ano atual
    anoAtual = date.today().year

    #calculo idade
    idade = pessoa1.idade(anoAtual, nascimeto)

    os.system('cls')

    #Saída
    print('='*40)
    print(f'Nome: {pessoa1.nome}')
    print(f'Idade: {idade}')
    print('='*40)

    pergunta = str(input('Deseja rodar novamente (s/n): '))
    if pergunta != 's' and pergunta != 'n':
        print('Inválido')
    elif pergunta == 's':
        os.system('cls')
        print('-'*80)
        print('')
        print('='*80)
        continue
    else:
        break