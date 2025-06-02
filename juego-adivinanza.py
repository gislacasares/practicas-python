import random


numero_secreto = random.randint(1,99)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("bienvenido al juego de adivinar el nro secreto")

while not adivinado and cant_intentos < cant_max_intentos :
    entrada = input("Introduce un nro del 1 al 99: ") # TODO: se debe convertir a numero ya que la function devuelve string
    numero = int(entrada)

    if(numero == numero_secreto):
        print("ADIVINASTE! el numero era: ", numero_secreto)
        adivinado = True
    elif numero < numero_secreto:
        print("el nro es mayor al ingresado")
    else:
        print("el nro es menor al ingresado")
    
    cant_intentos += 1

if not cant_intentos - cant_max_intentos:
    print("Perdiste, se acabaron los intentos")