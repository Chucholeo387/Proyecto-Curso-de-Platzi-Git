
import random

def  Adivina_el_numero(x):
    

    print("=====================================")
    print("Bienvenido al juego adivina el numero")
    print("=====================================")

    numero_aleatorio = random.randint(1, x)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}:  "))

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. El numero es muy pequenho")
        elif prediccion > numero_aleatorio:
            print("Intentalo otra vez. El numero es muy grande")


    print("========================================================")
    print(f"felicidades, has adivinado el numero {numero_aleatorio}")
    print("========================================================")



Adivina_el_numero(50)