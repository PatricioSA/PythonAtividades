def soma(a, b):
    s = a + b
    return '+',  s

def subtracao(a, b):
    s = a - b
    return '-', s

def produto(a, b):
    p = a * b
    return '*', p

def divisao(a, b):
    d = a / b
    return '/', d

def divisao_inteira(a, b):
    di = a // b
    return '//', di

def resto_divisao(a, b):
    rd = a % b
    return '%', rd