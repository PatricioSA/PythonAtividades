from email.errors import MalformedHeaderDefect
import os

from carro import Carro


os.system('cls')

#Entrada de dados
marca = str(input('Digite a marca: ')).capitalize
placa = str(input('Digite a placa: '))
ano = int(input('Digite o ano: '))
velocidade = int(input('Digite sua velocidade: '))

#Intanciando objeto
carro1 = Carro(marca, placa, ano)

teste = carro1.andar(velocidade)

os.system('cls')

#Saída
print('='*40)
print(f'Marca: {carro1.marca}')
print(f'Placa: {carro1.placa}')
print(f'Ano: {carro1.ano}')
print()
print(teste)
print('='*40)