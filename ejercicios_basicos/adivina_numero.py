import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("Bienvenido al juego 'Adivina el número'.")
    print("He pensado en un número entre 1 y 100. ¡Adivina cuál es!")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivina_el_numero()

