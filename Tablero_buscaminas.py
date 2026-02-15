# Tablero.py

def tablero_vacio(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def hacer_tablero_visible(filas, columnas):
    return [["." for _ in range(columnas)] for _ in range(filas)]

def mostrar_tablero(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])

    print("  ", end="")
    for c in range(columnas):
        print(c, end=" ")
    print()

    for f in range(filas):
        print(f, end=" ")
        for c in range(columnas):
            print(tablero[f][c], end=" ")
        print()

def destapar(tablero_jugador, tablero_oculto, f, c):
    tablero_jugador[f][c] = tablero_oculto[f][c]

def marcar(tablero_jugador, f, c):
    tablero_jugador[f][c] = "F"

def desmarcar(tablero_jugador, f, c):
    tablero_jugador[f][c] = "."
