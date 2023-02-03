import random

class Carta:
    palos = ['C', 'D', 'T', 'P']
    numeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    cartas = []

    def __init__(self):
        self._crear()
        pass

    def _crear(self):
        for p in self.palos:
            for n in self.numeros:
                self.cartas.append(n+p)

    def cogerUna(self):
        index = random.randint(0, len(self.cartas) - 1)
        return self.cartas.pop(index)

    def mostrar(self):
        print(self.cartas)