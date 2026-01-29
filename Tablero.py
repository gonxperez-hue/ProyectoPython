# Código del tablero

import random

filas = 6
columnas = 6
num_minas_facil = 3
num_minas_medio = 5
num_minas_dificil = 7

# Esto sirve para generar un tablero vacio, no va a ser el que se enseñará cuando ejecute el codigo
# Aqui es donde se van a añadir las minas 

def tablero_vacio(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = [0] * columnas #Esto crea una fila llena de 0
        tablero.append(fila) #Añade la fila al tablero
    return tablero


# Esto va a generar el tablero que si va a ver el ususario.
# En este tablero es donde van a estar todas las casillas ocultas

def hacer_tablero_visible(filas, columnas):
    tablero = []
    for filas in range(filas):
        fila = ["."] * columnas
        tablero.append(fila)
    return tablero


tablero_visible = hacer_tablero_visible(6,6)

for fila in tablero_visible:
    print(fila)
    
def mostrar_tablero(tablero_visible):
    filas = len(tablero_visible) # Numero total de filas y de columnas
    columnas = len(tablero_visible[0])
    
    print(" ", end="") # Es un espacio inicial para alinear con los números de la de la fila
    for columna in range(columnas):
        print(columna, end=" ")
    print() # Esto es un salto de linea, igual que el que hay abajo
    
    for fila in range(filas):
        print(fila, end=" ")
        for j in range(columnas):
            print(tablero_visible[fila][j], end=" ")
        print()
        
#Esto es todo el código del tablero, ahora tenemmos que integrar las funciones de las minas con este codigo y ver que todo funcione