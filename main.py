from blackjack.mesa import Mesa
from ruleta.juego import Juego

while True:
    print("Menu:")
    print("1. Entrar a la Ruleta")
    print("2. Entrar al blackjack")
    print("3. Salir")
    choice = input("Elige una opción: ")

    if choice == '1':
        Juego()
    elif choice == '2':
        Mesa()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")

print("Saliendo...")