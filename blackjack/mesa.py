from blackjack import carta, juagador
class Mesa:
    baraja = carta.Carta()
    player = juagador.Jugador()
    crupiere = juagador.Jugador()

    def __init__(self):
        self._crupiereInit()
        self._playerInit()
        self._playerJuego()
        self._crupiereJuego()
        print('Fin de la partida')
        pass

    def _crupiereInit(self):
        self.crupiere.cogerCarta(self.baraja.cogerUna())
        self.crupiere.cogerCarta(self.baraja.cogerUna())
        self.mostrar()

    def _playerInit(self):
        self.player.cogerCarta(self.baraja.cogerUna())
        self.player.cogerCarta(self.baraja.cogerUna())
        self.player.mostrar()

    def _playerJuego(self):
        while self.player.alive:
            print('Quieres pasar(P) o quieres coger(C)?')
            response = input()
            if (response == 'P'):
                return
            
            print('Quieres apostar?(Y/n)')
            response = input()

            self.player.cogerCarta(self.baraja.cogerUna())
            self.mostrar()
            self.player.mostrar()

    def _crupiereJuego(self):
        while self.player.alive and self.crupiere.alive:
            print('Juega el crupier, ver juego')
            input()

            self.player.cogerCarta(self.baraja.cogerUna())
            self.mostrar()
            self.player.mostrar()


    def mostrar(self):
        print('Crupiere: ' + self.crupiere.cartas[0])
