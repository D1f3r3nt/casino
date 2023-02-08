from blackjack.banco import Banco

class Jugador:
    cartas = []
    puntos = 0
    alive = True
    nombre = ""
    _restas = 0
    dinero = Banco()

    def __init__(self, nombre):
        self.cartas = []
        self.puntos = 0
        self.alive = True
        self.nombre = nombre
        self._restas = 0
        pass

    def cogerCarta(self, carta):
        self.cartas.append(carta)
        valor = carta[:-1]

        if (valor == 'J' or valor == 'Q' or valor == 'K'):
            valor = 10
        elif (valor == 'A'):
            valor = 11
            self._restas += 1

        self.puntos += int(valor)

        while self.puntos > 21 and self._restas > 0:
            self.puntos -= 10
            self._restas -= 1

        if (self.puntos > 21):
            self.alive = False

    def mostrar(self):
        print(self.nombre + ' (' + str(self.puntos) + 'p) : ')
        for carta in self.cartas:
            print('==> ' + carta)

    def mostarSoloPrimera(self):
        print(self.nombre + ' : ')
        print('==> ' + self.cartas[0])