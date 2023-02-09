import random
class Ruleta:
    def __init__(self):
        self.numeros = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.colores = ['V', 'R', 'N', 'R', 'N', 'R', 'N', 'R', 'N', 'R', 'N', 'N', 'R', 'N', 'R', 'N', 'R', 'N', 'R', 'R', 'N', 'R', 'N', 'R', 'N', 'R', 'N', 'N', 'R', 'N', 'R', 'N', 'R']
        
        self.numerorandom = random.choice(self.numeros)
        self.colorandom = random.choice(self.colores)