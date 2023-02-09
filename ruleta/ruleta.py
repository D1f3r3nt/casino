import random
class Ruleta:
    def __init__(self):
        self.SALDOINICIAL = 50000
        self.numeros = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.colores = ['verde', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo']
        
        self.numerorandom = random.choice(self.numeros)
        self.colorandom = random.choice(self.colores)