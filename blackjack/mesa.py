import time
from blackjack.carta import Carta
from blackjack.jugador import Jugador
class Mesa:
    baraja = Carta()
    player = Jugador('Jugador')
    crupiere = Jugador('Crupiere')

    def __init__(self):
        if (self._entrada()):
            self._crupiereInit()
            self._playerInit()
            self._playerJuego()
            self._crupiereJuego()
            self._finPartida()
        pass

    def _entrada(self):
        print('Bienvenido al blackjack')
        while True:
            print('Que quieres apostar? (min. 5)')
            apuesta = input('==> ')
            if (apuesta.isnumeric()):
                if (int(apuesta) >= 5):
                    if (self.player.dinero.apostarDinero(int(apuesta))):
                        print('==========================================')
                        print()
                        break
                    else:
                        print('No tienes tanto saldo')
                        print('Quieres salir? (exit)')
                        res = input('==> ')
                        if (res == "exit"):
                            return False
        return True
        

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
            print('Quieres pasar(P), coger(C) o doblar(D)?')
            response = input()
            if (response == 'P'):
                return

            self.player.cogerCarta(self.baraja.cogerUna())
            self.crupiere.mostarSoloPrimera()
            self.player.mostrar()

            if (response == 'D'):
                self.player.dinero.doblarApuesta()
                break
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
        if self.player.alive == False or (self.crupiere.puntos > self.player.puntos and self.crupiere.alive == True):
            print('Gana la casa')
            self.player.dinero.hasGanado(False)
        elif self.crupiere.alive == False or self.crupiere.puntos < self.player.puntos:
            print('Gana el jugador')
            self.player.dinero.hasGanado(True)
        else:
            print('EMPATE')
        print()
        print('==========================================')
        print(str(self.player.dinero.dinero) + ' €')
        print()