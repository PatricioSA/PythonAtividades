class Pessoa:
    
    def __init__(self, nome, anoNascimento):
        self.nome = nome
        self.anoNascimento = anoNascimento

    def idade(self, anoAtual, anoNascimento):

        return anoAtual - anoNascimento
        

    