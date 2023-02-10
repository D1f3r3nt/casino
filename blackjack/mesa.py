import time
from blackjack.carta import Carta
from blackjack.jugador import Jugador

class Mesa:
    def __init__(self, saldo):
        self.baraja = Carta()
        self.player = Jugador('Jugador', saldo)
        self.crupiere = Jugador('Crupiere', saldo)

        if (self._entrada()):
            self._crupiereInit()
            self._playerInit()
            self._playerJuego()
            self._crupiereJuego()
            self._finPartida()
        pass

    def _entrada(self):
        print('Bienvenido al blackjack')
        print(f'Tu saldo es de {self.player.banco.dinero} €')
        while True:
            print('Que quieres apostar? (min. 5)')
            apuesta = input('==> ')
            if (apuesta.isnumeric() and int(apuesta) >= 5):
                if (self.player.banco.apostarDinero(int(apuesta))):
                    print('==========================================')
                    print()
                    break
                else:
                    print('No tienes tanto saldo')
                    print('Quieres salir? (exit)')
                    res = input('==> ').lower()
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
            print()
            print('==========================================')
            print()
            print('Quieres pasar(P), coger(C) o doblar(D)?')
            response = input("==> ").upper()
            if (response != 'P' and response != 'C' and response != 'D'):
                print("No te he entendido")
                continue

            if (response == 'P'):
                break

            self.player.cogerCarta(self.baraja.cogerUna())
            self.crupiere.mostarSoloPrimera()
            self.player.mostrar()

            if (response == 'D'):
                if (self.player.banco.doblarApuesta() == False):
                    print('No se ha podido doblar, no hay saldo')
                break

        time.sleep(2)
        print()
        print('==========================================')
        print()

    def _crupiereJuego(self):
        print('Juega el crupier, ver juego')
        self.crupiere.mostrar()
        self.player.mostrar()
        print()
        print('==========================================')
        print()

        while self.player.alive and self.crupiere.alive and self.crupiere.puntos < 17:
            time.sleep(2)
            self.crupiere.cogerCarta(self.baraja.cogerUna())
            self.crupiere.mostrar()
            self.player.mostrar()
            print()
            print('==========================================')
            print()

    def _finPartida(self):
        print("...")
        time.sleep(5)
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
            self.player.banco.hasGanado(False)
        elif self.crupiere.alive == False or self.crupiere.puntos < self.player.puntos:
            print('Gana el jugador')
            self.player.banco.hasGanado(True)
        else:
            print('EMPATE')
        print()
        print('==========================================')
        print()