import random

# =========
#  MINAS
# =========

# Preguntamos al usuario qué modo quiere usar
def elegir_dificultad():
    print("Elige dificultad:")
    print("1. Fácil (3 minas)")
    print("2. Medio (5 minas)")

    opcion = input("Opción: ")

    if opcion == "1":
        return 3   # Modo Fácil
    elif opcion == "2":
        return 5   # Modo Medio
    else:
        print("Opción no válida, se usará modo fácil.")
        return 3


# Genera las minas en posiciones aleatorias sin repetir
def generar_minas(filas=6, columnas=6, cantidad=3):
    minas = set() # El set nos va a evitar que se repitan posiciones
    while len(minas) < cantidad:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        minas.add((f, c))
    return minas


# Coloca las minas en el tablero marcando con 'M'
def colocar_minas(tablero, minas):
    for f, c in minas:
        tablero[f][c] = "M"


# Calcula cuántas minas hay alrededor de cada casilla
def calcular_numeros(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])

    for f in range(filas):
        for c in range(columnas):

            # Si es una mina, no se calcula nada
            if tablero[f][c] == "M":
                continue

            contador = 0

            # Arriba
            if f > 0 and tablero[f-1][c] == "M":
                contador += 1

            # Abajo
            if f < filas - 1 and tablero[f+1][c] == "M":
                contador += 1

            # Izquierda
            if c > 0 and tablero[f][c-1] == "M":
                contador += 1

            # Derecha
            if c < columnas - 1 and tablero[f][c+1] == "M":
                contador += 1

            # Diagonal arriba-izquierda
            if f > 0 and c > 0 and tablero[f-1][c-1] == "M":
                contador += 1

            # Diagonal arriba-derecha
            if f > 0 and c < columnas - 1 and tablero[f-1][c+1] == "M":
                contador += 1

            # Diagonal abajo-izquierda
            if f < filas - 1 and c > 0 and tablero[f+1][c-1] == "M":
                contador += 1

            # Diagonal abajo-derecha
            if f < filas - 1 and c < columnas - 1 and tablero[f+1][c+1] == "M":
                contador += 1

            # Guardamos el número final en la casilla
            tablero[f][c] = str(contador)