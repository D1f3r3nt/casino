from banco import Banco

# Creamos la clase jugador donde le establecemos sus parametros
class Jugador:
    cartas = []
    puntos = 0
    alive = True
    nombre = ""
    _restas = 0

    # Se inicia la logica donde interactuan los participante y mostrara los datos 
    def __init__(self, nombre, saldo):
        self.cartas = []
        self.puntos = 0
        self.alive = True
        self.nombre = nombre
        self._restas = 0
        self.banco = saldo
        pass

    # Funcion donde  se coge carta junto a un control donde para controlar el As ya que tiene dos valores, 
    # dependiendo las cartas que tengamos al tener tanto el valor de 11 o de 1.
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
            
    # Funcion que mostrara el nombre de las cartas almacenadas  asi como los puntos que tenga el jugador
    def mostrar(self):
        print(self.nombre + ' (' + str(self.puntos) + 'p) : ')
        for carta in self.cartas:
            print('==> ' + carta)
            
    # Funcion para mostrar unicamente una carta mientras el proceso de juego del jugador este en curso
    def mostarSoloPrimera(self):
        print(self.nombre + ' : ')
        print('==> ' + self.cartas[0])