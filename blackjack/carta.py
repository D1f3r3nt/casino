import random

# En esta clase creamos las cartas del blackjack y sus correspondientes palos 
class Carta:
    palos = ['C', 'D', 'T', 'P']
    numeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    cartas = []

    # Funcion que inicia crear
    def __init__(self):
        self._crear()
        pass

    
    # inicia la funcion crear donde guardara palos y numeros  durante la partida
    
    def _crear(self):
        for p in self.palos:
            for n in self.numeros:
                self.cartas.append(n+p)
                
    # De lo que se ha almacenado en cartas[] a traves del metodo random hacemos que nos retorne 
    # la carta tanto numero como palo
    def cogerUna(self):
        index = random.randint(0, len(self.cartas) - 1)
        return self.cartas.pop(index)

    # Funcion que muestra las cartas "almacenadas" dentro de la array vacia
    def mostrar(self):
        print(self.cartas)