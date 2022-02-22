class Salario:

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aumento(salario):
        cinco = (5 / 100 * salario) + salario
        dez = (10 / 100 * salario) + salario
        if (salario > 1500):
            return cinco
        elif (salario < 1000):
            return dez

