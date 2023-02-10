# Esta clase sirve para controlar el tema de apuestas y del dinero
class Banco:
    dinero = 100
    apuesta = 0
    apuesta2 = 0

    def __init__(self, dinero):
        self.dinero = dinero
        self.apuesta = 0
        self.apuesta2 = 0
        pass

    # Este metodo nos sirve para apostar dinero y ademas controla
    # que sea viable la apuesta, devuelve un booleano indicando si a sido posible
    def apostarDinero(self, cantidad):
        if (cantidad > self.dinero):
            return False
        else:
            self.apuesta = cantidad
            return True

    # Este metodo nos sirve para apostar dinero y ademas controla
    # que sea viable la apuesta, devuelve un booleano indicando si a sido posible
    def apostarDineroColor(self, cantidad):
        if (cantidad > (self.dinero - self.apuesta)):
            return False
        else:
            self.apuesta2 = cantidad
            return True
        
    # Este metodo nos sirve para doblar la apuesta y ademas controla
    # que sea viable la apuesta, devuelve un booleano indicando si a sido posible
    def doblarApuesta(self):
        if (self.dinero >= self.apuesta * 2):
            self.apuesta *= 2
            return True
        else:
            return False

    # A este metodo se la pasa un booleano para indicar si ha ganado o no
    # Realizara una funcion diiferente dependiendo de lo que sea
    def hasGanado(self, resultado):
        if resultado:
            self.dinero += self.apuesta
        else:
            self.dinero -= self.apuesta
        self.apuesta = 0

    # A este metodo se la pasa un booleano para indicar si ha ganado o no
    # Realizara una funcion diiferente dependiendo de lo que sea
    # Ademas multiplica * 36 ya que es el premio por acertar el numero
    def hasGanadoNumero(self, resultado):
        if resultado:
            self.dinero += self.apuesta * 36
        else:
            self.dinero -= self.apuesta
        self.apuesta = 0

    # A este metodo se la pasa un booleano para indicar si ha ganado o no
    # Realizara una funcion diiferente dependiendo de lo que sea
    def hasGanadoColor(self, resultado):
        if resultado:
            self.dinero += self.apuesta2
        else:
            self.dinero -= self.apuesta2
        self.apuesta2 = 0
        