import os
import time

from blackjack.mesa import Mesa
from ruleta.juego import Juego
from banco import Banco

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show():
    print("""
                 _             
                (_)            
      ___ __ _ ___ _ _ __   ___  
     / __/ _` / __| | '_ \ / _ \ 
    | (_| (_| \__ \ | | | | (_) |
     \___\__,_|___/_|_| |_|\___/ 
    """)

saldo = Banco(100)

while True:
    clear()
    show()
    print("==============================================")
    print(f"Tu saldo es de {saldo.dinero} €")
    print("Menu:")
    print("1. Entrar a la Ruleta")
    print("2. Entrar al blackjack")
    print("3. Salir")
    print("==============================================")
    choice = input("==> ")

    if choice == '1':
        clear()
        Juego(saldo)
        time.sleep(5)
    elif choice == '2':
        clear()
        Mesa(saldo)
        time.sleep(5)
    elif choice == '3':
        break

print("Saliendo...")



