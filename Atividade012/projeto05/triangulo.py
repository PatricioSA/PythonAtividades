class Triangulo:

    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def condicao_existencia(lado1, lado2, lado3):
        teste = 'Formam um triângulo'
        teste3 = 'Não formam um triângulo'
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) \
    and (lado2 + lado3 > lado1):
            return teste
        else:
            return teste3

    def perimetro(lado1, lado2, lado3):  #P = l+l+l
        p = lado1 + lado2 + lado3
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) \
    and (lado2 + lado3 > lado1):
            return p