import random

#Declaramos variables globales para el juego 
FILAS = 9
COLUMNAS = 9
MAR = " "
SUBMARINO = "S" #Ocupa una celda
DESTRUCTOR = "D" #Ocupa dos celdas
DESTRUCTOR_VERTICAL = "DV" #Ocupa dos celdas de manera vertical
DISPARO_FALLIDO = "-"
DISPARO_ACERTADO = "*"
DISPAROS_INICIALES = 10
CANTIDAD_BARCOS_INICIALES = 8
JUGADOR_1 = "J1"
JUGADOR_2 = "J2"


#Declaramos la funcion para obtener la matriz inicial del juego
def obtener_matriz_inicial():
    matriz = []
    for y in range(FILAS):
        #Agregamos un arreglo a la matriz, que seria una fila basicamente
        matriz.append([])
        for x in range(COLUMNAS):
            #Acto seguido agregamos una celda a esa fila. Por defecto lleva "Mar"
            matriz[y].append(MAR) 
    return matriz

#Con esta función al sumar 1 a una letra obtenemos la siguiente letra en el abecedario
def incrementar_letra(letra):
    return chr(ord(letra) + 1)


def imprimir_separador_horizontal():
    #Imprimir un renglón dependiendo de las columnas que haya
    for _ in range(COLUMNAS + 1):
        print("+----", end="")
    print("+")


def imprimir_fila_numeros():
    print("     ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print(" | ")


#Función que indica si una coordenada de la matriz esta vacia
def es_mar(x, y, matriz):
    return matriz[y][x] == MAR


def coordenada_en_rango(x, y):
    return x > 0 and x < COLUMNAS -1 and y > 0 and y < FILAS -1


#Dividimos y redondeamos a entero hacia abajo (ya que no podemos colocar una parte no entera de un barco)
def obtener_e_imprimir_barcos (matriz, cantidad_barcos, jugador):
    barcos_una_celda = cantidad_barcos // 2
    barcos_dos_celdas_verticales = cantidad_barcos // 4
    barcos_dos_celdas_horizontales = cantidad_barcos // 4
    if jugador == JUGADOR_1:
        print ("Imprimiendo barcos del jugador 1")
    else:
        print ("Imprimiendo barcos del jugador 2")
    print(f"Barcos de una celda: {barcos_una_celda}\nBarcos verticales de dos celdas: {barcos_dos_celdas_verticales}")
    #Primero colocamos los de dos celdas para que se acomoden bien
    matriz = colocar_barcos_de_dos_celdas_horizontal(
        barcos_dos_celdas_horizontales, DESTRUCTOR, matriz)
    matriz = colocar_barcos_de_dos_celdas_vertical(
        barcos_dos_celdas_verticales, DESTRUCTOR_VERTICAL, matriz)
    matriz = colocar_barcos_de_una_celda(barcos_una_celda, SUBMARINO, matriz)
    return matriz
























