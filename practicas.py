#--------Adivina el numero--------
import random
def adivina(n):
    print("=================")
    print("JUGUEMOS")
    print("=================")
    numero=""
    aleatorio = random.randint(0,n)
    intento = 0

    while numero != aleatorio and intento <= 11:
        numero = int(input("Dime un numero: "))
        if numero == aleatorio:
            print("Felicidades has encontrado el numero")

        elif numero < aleatorio:
            
            print("Tu numero es mas bajo")
            
        elif numero > aleatorio:
            print("Tu numero es mas alto")

        elif intento == 10:
            print("Lo siento tus intentos se han terminado")
            break
            
        else:
            print("Lo siento no lo has conseguido")

        intento += 1

adivina(100)
