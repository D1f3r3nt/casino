class Banco:
    dinero = 100
    apuesta = 0
    apuesta2 = 0

    def __init__(self, dinero):
        self.dinero = dinero
        self.apuesta = 0
        self.apuesta2 = 0
        pass

    def apostarDinero(self, cantidad):
        if (cantidad > self.dinero):
            return False
        else:
            self.apuesta = cantidad
            return True

    def apostarDineroColor(self, cantidad):
        if (cantidad > (self.dinero - self.apuesta)):
            return False
        else:
            self.apuesta2 = cantidad
            return True
        
    def doblarApuesta(self):
        self.apuesta *= 2

    def hasGanado(self, resultado):
        if resultado:
            self.dinero += self.apuesta
        else:
            self.dinero -= self.apuesta
        self.apuesta = 0

    def hasGanadoNumero(self, resultado):
        if resultado:
            self.dinero += self.apuesta * 36
        else:
            self.dinero -= self.apuesta
        self.apuesta = 0

    def hasGanadoColor(self, resultado):
        if resultado:
            self.dinero += self.apuesta2
        else:
            self.dinero -= self.apuesta2
        self.apuesta2 = 0
        