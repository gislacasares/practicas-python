nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input("Hola jugador 1, que elijes? ¿Piedra, Papel o tijeras??: ")
jugador2 = input("Hola jugador 2, que elijes? ¿Piedra, Papel o tijeras??: ")

if jugador1 == jugador2:
    print("han empatado")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ganó el jugador ", nombre1)
else:
    print("Ganó el jugador ", nombre2)
