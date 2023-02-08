class Banco:
    dinero = 100
    apuesta = 0

    def __init__(self):
        self.dinero = 100
        self.apuesta = 0
        pass

    def apostarDinero(self, cantidad):
        if (cantidad > self.dinero):
            return False
        else:
            self.apuesta = cantidad
            return True
        
    def doblarApuesta(self):
        self.apuesta *= 2

    def hasGanado(self, resultado):
        if resultado:
            self.dinero += self.apuesta
        else:
            self.dinero -= self.apuesta
        