import time
from blackjack import carta, juagador
class Mesa:
    baraja = carta.Carta()
    player = juagador.Jugador('Jugador')
    crupiere = juagador.Jugador('Crupiere')

    def __init__(self):
        self._crupiereInit()
        self._playerInit()
        self._playerJuego()
        self._crupiereJuego()
        self._finPartida()
        pass

    def _crupiereInit(self):
        self.crupiere.cogerCarta(self.baraja.cogerUna())
        self.crupiere.cogerCarta(self.baraja.cogerUna())
        self.crupiere.mostarSoloPrimera()

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
            self.crupiere.mostarSoloPrimera()
            self.player.mostrar()
        time.sleep(2)

    def _crupiereJuego(self):
        while self.player.alive and self.crupiere.alive and self.crupiere.puntos < 17:
            print('Juega el crupier, ver juego')
            input()

            self.crupiere.cogerCarta(self.baraja.cogerUna())
            self.crupiere.mostrar()
            self.player.mostrar()
        time.sleep(2)

    def _finPartida(self):
        print()
        print('==========================================')
        print('==========================================')
        print()
        self.crupiere.mostrar()
        self.player.mostrar()
        print()
        print('==========================================')
        print()
        print('Fin de la partida')
        print()
        if self.player.alive == False or self.crupiere.puntos > self.player.puntos:
            print('Gana la casa')
        elif self.crupiere.alive == False or self.crupiere.puntos < self.player.puntos:
            print('Gana el jugador')
        else:
            print('EMPATE')
        print()
        print('==========================================')
        print()