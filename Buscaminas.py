# Código del juego Buscaminas

import random

filas = 6
columnas = 6
num_minas_facil = 3
num_minas_medio = 5
num_minas_dificil = 7

# Esto sirve para generar un tablero vacio, no va a ser el que se enseñará cuando ejecute el codigo

def tablero_vacio(filas, columnas):
    tablero = []
    for fila in range(filas):
        fila = [0] * columnas
        tablero.append(fila)
    return tablero

print(tablero_vacio(6, 6)) #Esto es temporal, solo para ver que funciona el tablero 