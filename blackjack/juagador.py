class Jugador:
    cartas = []
    puntos = 0
    alive = True

    def __init__(self):
        pass

    def cogerCarta(self, carta):
        self.cartas.append(carta)
        valor = carta[:-1]
        if (valor == 'J' or valor == 'Q' or valor == 'K'):
            valor = 10
        elif (valor == 'A'):
            valor = 1
            # Modificar valor propero

        self.puntos += int(valor)

        if (self.puntos > 21):
            self.alive = False

    def mostrar(self):
        print('Jugador(' + str(self.puntos) + 'p): ')
        for carta in self.cartas:
            print('==> ' + carta)
