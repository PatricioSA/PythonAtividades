#Curso Técnico de Informática
#Autor: Patrício Samuel
#Data início: 26/10/2021
#Término: 26/10/2021
#Atividade 001

#declaração e entrada
nome = str(input('Qual o seu nome: '))
dataNascimento = int(input('Em que ano você nasceu: '))
rg = str(input('Qual seu RG: '))
cpf = int(input('Qual seu CPF: '))
rua = str(input('Qual é sua rua: '))
numero = int(input('Número da sua casa: '))
complemento = str(input('Qual o complemento: '))
cep = int(input('Qual seu CEP: '))
cidade = str(input('Qual sua cidade: '))
estado = str(input('Qual seu Estado: '))
pais = str(input('Qual seu país: '))

#Saída
print('='*40)
print('Dados Pessoais')
print('Nome:', nome)
print('Data de nascimento:', dataNascimento)
print('RG:', rg)
print('CPF:', cpf)
print('-'*40)
print('Endereço')
print('Rua:', rua)
print('Número:', numero)
print('Complemento:', complemento)
print('CEP:', cep)
print('Cidade:', cidade)
print('Estado:', estado)
print('País:', pais)