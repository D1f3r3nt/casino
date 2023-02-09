from contextlib import nullcontext
import random
class Ruleta:
    def __init__(self):
        self.SALDOINICIAL = 50000
        self.superandom = random
        self.NUMEROS = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.COLORES = ['verde', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'negro', 'rojo', 'negro', 'rojo', 'negro', 'rojo']
        self.numerorandom = self.superandom.choice(self.NUMEROS)
        self.colorandom = self.superandom.choice(self.COLORES)

def main_menu():
    print("Menu:")
    print("1. Entrar a la Ruleta")
    print("2. Salir")
    choice = input("Elige una opción: ")

    if choice == '1':
        app()
    elif choice == '2':
        print("Saliendo...")
    else:
        print("Invalid choice. Try again.")
        main_menu()
            
def app():
    ruleta = Ruleta()

    colores = ['negro', 'rojo', 'verde', 'black', 'red', 'green', 'negre', 'vermell', 'verd']
    color_map = {"black": "negro", "negre": "negro", "red": "rojo", "vermell": "rojo", "green": "verde", "verd": "verde"}
    flag = True

    while ruleta.SALDOINICIAL > 0:
        try:
            dinero_apostadoNum = float(input(f"¿Cuánto apuestas? no debe superar el saldo: Tu saldo es {ruleta.SALDOINICIAL}: "))
            if dinero_apostadoNum > ruleta.SALDOINICIAL or dinero_apostadoNum < 0:
                print(f"No puedes apostar más de lo que tienes en tu saldo.")
            else:
                saldo = ruleta.SALDOINICIAL - dinero_apostadoNum
                break
        except ValueError:
            print(f"El valor ingresado debe ser un número.")
   
    while True:
        try:
            eleccionNum = int(input(f"A que numero quieres apostar? Recuerda que los numeros van del 0 al 36 ambos incluidos: "))
            if 0 <= eleccionNum <= 36:
                break
        except ValueError:
            print(f"El valor ingresado debe ser un número.")

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

    eleccionColor = "lila"
        
    if apostarNumero > 0:
        while flag:
            eleccionColor = input(f"A que color quieres apostar? Recuerda que hay Negro, Rojo y Verde: ")
            for i in colores:
                if eleccionColor.__eq__(i):
                    eleccionColor = color_map.get(eleccionColor.lower(), None)
                    flag = False
                    break
    
    if eleccionNum == ruleta.numerorandom:
        ganancias_numero = dinero_apostadoNum * 36
        #eleccionColor = color_map_ES.get(eleccionColor.lower(), None)
    else:
        ganancias_numero =- dinero_apostadoNum
        
    if eleccionColor == ruleta.colorandom:
        ganancias_color = apostarNumero*2
    else:
        ganancias_color =- apostarNumero
    print(f"HA TOCADO --> {ruleta.numerorandom}, {ruleta.colorandom}")
    print(f"Has obtenido {ganancias_numero}€ del numero, {ganancias_color}€ de color")
    if (ganancias_color+ganancias_numero)>0:
        #ruleta.SALDOINICIAL = saldo +(ganancias_numero+ganancias_color)
        print(f"El total ganado ha sido --> {ganancias_numero+ganancias_color}€")
        print(f"Saldo actual: {saldo}")
        print("ENHORABUENA!!!")
    else:
        #ruleta.SALDOINICIAL = saldo -(ganancias_numero+ganancias_color)
        print(f"El total PERDIDO ha sido --> {ganancias_numero+ganancias_color}€")
        print(f"Saldo actual: {saldo}")
        print("MALA SUERTE!!!")

main_menu()