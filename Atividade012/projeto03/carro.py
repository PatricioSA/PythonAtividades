from re import A


class Carro:

    def __init__(self, marca, placa, ano):
        self.marca = marca
        self.placa = placa
        self.ano = ano

    def andar(self, velocidade):
        if (velocidade < 60):
            return 'VELOCIDADE PERMITIDA!'
        else:
            return 'SUA VELOCIDADE ESTÁ ACIMA DA PERMITIDA!'