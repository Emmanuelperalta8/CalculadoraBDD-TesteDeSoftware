import math

class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return b - a

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

    def raiz_quadrada(self, n):
        if n < 0:
            raise ValueError("Número inválido")
        return math.sqrt(n)

    def media(self, lista):
        if len(lista) == 0:
            raise ValueError("Número inválido")
        return sum(lista) / len(lista)
