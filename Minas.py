# Minas.py
import random

# Genera 'cantidad' de minas en posiciones aleatorias sin repetir
def generar_minas(filas=6, columnas=6, cantidad=3):
    minas = set()
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

            if tablero[f][c] == "M":
                continue

            contador = 0

            # Revisar las 8 direcciones
            for df in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if df == 0 and dc == 0:
                        continue
                    nf, nc = f + df, c + dc
                    if 0 <= nf < filas and 0 <= nc < columnas:
                        if tablero[nf][nc] == "M":
                            contador += 1

            tablero[f][c] = str(contador)
