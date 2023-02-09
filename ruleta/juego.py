import time
from ruleta.ruleta import Ruleta
from ruleta.jugador import Jugador

class Juego:    
    def __init__(self, saldo):
        self.ruleta = Ruleta()
        self.jugador = Jugador(saldo)

        self.dineroApostadoNum = 0
        self.eleccionNum = 0
        self.dineroApostadoColor = 0
        self.eleccionColor = ""
        self.dinero = self.jugador.banco.dinero

        self._apuestaNumero()
        self._numero()
        self._apuestaColor()
        self._color()
        self._girarRuleta()
        self._resultados()
        pass

    def _apuestaNumero(self):
        while self.jugador.banco.dinero > 0:
            try:
                print(f"Tu saldo es {self.jugador.banco.dinero} €")
                print(f"¿Cuánto apuestas? (min 0)")
                self.dineroApostadoNum = int(input("==> "))
                if self.jugador.banco.apostarDinero(self.dineroApostadoNum) and self.dineroApostadoNum >= 0:
                    self.dinero -= self.dineroApostadoNum
                    break
                else:
                    print(f"No puedes apostar más de lo que tienes en tu saldo.")
            except ValueError:
                print(f"El valor ingresado debe ser un número.")

    def _numero(self):
        while True:
            try:
                print(f"A que numero quieres apostar? (0-36) ")
                self.eleccionNum = int(input("==> "))
                if 0 <= self.eleccionNum <= 36:
                    break
            except ValueError:
                print(f"El valor ingresado debe ser un número.")

    def _apuestaColor(self):
        while True:
            try:
                print(f"Saldo actual: {self.dinero} €")
                print("Indica la cantidad que quieres apostar al Color: (min 0) ")
                self.dineroApostadoColor = int(input("==> "))
                if self.jugador.banco.apostarDineroColor(self.dineroApostadoColor) and self.dineroApostadoNum >= 0:
                    self.dinero -= self.dineroApostadoColor
                    break
                else: 
                    print(f"No puedes apostar más de lo que tienes en tu saldo.")
            except ValueError:
                print(f"El valor ingresado debe ser un número.")
        print(f"Saldo {self.dinero}")

    def _color(self):            
        if self.dineroApostadoColor > 0:
            while True:
                print(f"A que color quieres apostar Negro(N), Rojo(R) y Verde(V)?")
                self.eleccionColor = input("==> ")
                if (self.eleccionColor == "V" or self.eleccionColor == "R" or self.eleccionColor == "N"):
                    break
                print("Ponga un valor valido")
                        

    def _girarRuleta(self):
        self.jugador.banco.hasGanadoNumero(self.eleccionNum == self.ruleta.numerorandom)
        self.jugador.banco.hasGanadoColor(self.eleccionColor == self.ruleta.colorandom)

    def _resultados(self):
        print('...')
        time.sleep(5)
        print(f"HA SALIDO EL NUMERO: {self.ruleta.numerorandom}")
        print(f"HA SALIDO EL COLOR: {self._getColor(self.ruleta.colorandom)}")
        print(f"Saldo actual: {self.jugador.banco.dinero} €")
        print("GRACIAS POR JUGAR")

    def _getColor(self, letra):
        if letra == "V":
            return "Verde"
        if letra == "R":
            return "Rojo"
        return "Negro"