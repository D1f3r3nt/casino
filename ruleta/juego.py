from ruleta.ruleta import Ruleta

class Juego:
    ruleta = Ruleta()
    colores = ['negro', 'rojo', 'verde', 'black', 'red', 'green', 'negre', 'vermell', 'verd']
    color_map = {"black": "negro", "negre": "negro", "red": "rojo", "vermell": "rojo", "green": "verde", "verd": "verde"}
    flag = True
    dinero_apostadoNum = 0
    
    def __init__(self):
        self.ruleta = Ruleta()
        self.colores = ['negro', 'rojo', 'verde', 'black', 'red', 'green', 'negre', 'vermell', 'verd']
        self.color_map = {"black": "negro", "negre": "negro", "red": "rojo", "vermell": "rojo", "green": "verde", "verd": "verde"}
        self.flag = True
        self.dinero_apostadoNum = 0

        self._apuestaNumero()
        self._numero()
        self._apuestaColor()
        self._color()
        self._girarRuleta()
        self._resultados()
        pass

    def _apuestaNumero(self):
        while self.ruleta.SALDOINICIAL > 0:
            try:
                dinero_apostadoNum = float(input(f"¿Cuánto apuestas? no debe superar el saldo: Tu saldo es {self.ruleta.SALDOINICIAL}: "))
                if dinero_apostadoNum > self.ruleta.SALDOINICIAL or dinero_apostadoNum < 0:
                    print(f"No puedes apostar más de lo que tienes en tu saldo.")
                else:
                    saldo = self.ruleta.SALDOINICIAL - dinero_apostadoNum
                    break
            except ValueError:
                print(f"El valor ingresado debe ser un número.")

    def _numero(self):
        while True:
            try:
                eleccionNum = int(input(f"A que numero quieres apostar? Recuerda que los numeros van del 0 al 36 ambos incluidos: "))
                if 0 <= eleccionNum <= 36:
                    break
            except ValueError:
                print(f"El valor ingresado debe ser un número.")

    def _apuestaColor(self):
        while True:
            try:
                print(f"Saldo {saldo}")
                apostarNumero = int(input("Indica la cantidad que quieres apostar al Color: 0 si se quiere continuar sin apostar al color "))
                if 0 <= (saldo - apostarNumero):
                    break
            except ValueError:
                print(f"El valor ingresado debe ser un número.")
        saldo = saldo - apostarNumero
        print(f"Saldo {saldo}")

    def _color(self):
        eleccionColor = "lila"
            
        if apostarNumero > 0:
            while flag:
                eleccionColor = input(f"A que color quieres apostar? Recuerda que hay Negro, Rojo y Verde: ")
                for i in colores:
                    if eleccionColor.__eq__(i):
                        eleccionColor = color_map.get(eleccionColor.lower(), None)
                        flag = False
                        break

    def _girarRuleta(self):
        if eleccionNum == ruleta.numerorandom:
            ganancias_numero = dinero_apostadoNum * 36
            #eleccionColor = color_map_ES.get(eleccionColor.lower(), None)
        else:
            ganancias_numero =- dinero_apostadoNum
            
        if eleccionColor == ruleta.colorandom:
            ganancias_color = apostarNumero*2
        else:
            ganancias_color =- apostarNumero

    def _resultados(self):
        print(f"HA TOCADO --> {ruleta.numerorandom}, {ruleta.colorandom}")
        print(f"Has obtenido {ganancias_numero}€ del numero, {ganancias_color}€ de color")
        if (ganancias_color + ganancias_numero) > 0:
            #ruleta.SALDOINICIAL = saldo + (ganancias_numero+ganancias_color)
            print(f"El total ganado ha sido --> {ganancias_numero+ganancias_color}€")
            print(f"Saldo actual: {saldo}")
            print("ENHORABUENA!!!")
        else:
            #ruleta.SALDOINICIAL = saldo - (ganancias_numero+ganancias_color)
            print(f"El total PERDIDO ha sido --> {ganancias_numero+ganancias_color}€")
            print(f"Saldo actual: {saldo}")
            print("MALA SUERTE!!!")