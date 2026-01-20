import random

# ========
#  MINAS
# ========

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

