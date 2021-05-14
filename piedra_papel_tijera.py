print("""¡Hola! Este es el clásico juego de piedra, papel o tijera.""")

jugador_1 = input('¿Cuál es el nombre del jugador 1: ')
jugador_2 = input('¿Cuál es el nombre del jugador 2: ')

print('¿Listos?, suerte para ambos')

turno_1a = int(input(jugador_1 + ' '  + """
Elige una opción: 
1. piedra 
2. papel 
3. tijera: """))

turno_2b = int(input(jugador_2 + ' ' + """
Elige una opción: 
1. piedra 
2. papel 
3. tijera: """))

if turno_1a == turno_2b:
    print('Esto es un empate, ¡Qué reñida contienda!')
elif (turno_1a == 1 and turno_2b == 2) or (turno_1a == 2 and turno_2b == 3) or (turno_1a == 3 and turno_2b == 1):
    print('Gana ' + jugador_2 + ' ¡Felicidades!')
elif (turno_1a == 1 and turno_2b == 3) or (turno_1a == 2 and turno_2b == 1) or (turno_1a == 3 and turno_2b == 2):
    print('Gana ' + jugador_1 + ' ¡Felicidades!')
else:
    print('Elige una opción válida')



# if turno_1a == 1 and turno_2b == 1:
#     print('Esto es un empate, ¡Qué reñida contienda!')
# elif turno_1a == 1 and turno_2b == 2:
#     print('Gana ' + jugador_2 + ' ¡Felicidades!')
# elif turno_1a == 1 and turno_2b == 3:
#     print('Gana ' + jugador_1 + ' ¡Felicidades!')
# elif turno_1a == 2 and turno_2b == 2:
#     print('Esto es un empate, ¡Qué reñida contienda!')
# elif turno_1a == 2 and turno_2b == 3:
#     print('Gana ' + jugador_2 + ' ¡Felicidades!')
# elif turno_1a == 2 and turno_2b == 1:
#     print('Gana ' + jugador_1 + ' ¡Felicidades!')
# elif turno_1a == 3 and turno_2b == 3:
#     print('Esto es un empate, ¡Qué reñida contienda!')
# elif turno_1a == 3 and turno_2b == 1:
#     print('Gana ' + jugador_2 + ' ¡Felicidades!')
# elif turno_1a == 3 and turno_2b == 2:
#     print('Gana ' + jugador_1 + ' ¡Felicidades!')
# else:
#     print('Elige una opción válida')