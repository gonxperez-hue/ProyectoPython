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

#Funciones para colocar los barcos en la matriz de forma aleatoria
def obtener_x_aleatoria():
    return random.randint(0, COLUMNAS -1)

#Misma función que la anterior pero para la fila (y) en vez de la columna (x)
def obtener_y_aleatoria():
    return random.randint(0, FILAS -1)

#Función para colocar barcos de una celda 
def colocar_barcos_de_una_celda(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        if es_mar(x, y, matriz):
            matriz[y][x] = tipo_barco
            barcos_colocados += 1
            if barcos_colocados >= cantidad:
                break
    return matriz

#Función para colocar barcos de dos celdas en horizontal
def colocar_barcos_de_dos_celdas_horizontal(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        x2 = x + 1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x2, y) and es_mar(x, y, matriz) and es_mar(x2, y, matriz):
            matriz[y][x] = tipo_barco
            matriz[y][x2] = tipo_barco
            barcos_colocados += 1
            if barcos_colocados >= cantidad:
                break
    return matriz

#Función para colocar barcos de dos celdas en vertical
def colocar_barcos_de_dos_celdas_vertical(cantidad, tipo_barco, matriz):
    barcos_colocados = 0
    while True:
        x = obtener_x_aleatoria()
        y = obtener_y_aleatoria()
        y2 = y + 1
        if coordenada_en_rango(x, y) and coordenada_en_rango(x, y2) and es_mar(x, y, matriz) and es_mar(x, y2, matriz):
            matriz[y][x] = tipo_barco
            matriz[y2][x] = tipo_barco
            barcos_colocados += 1
            if barcos_colocados >= cantidad:
                break
    return matriz

#Función para imprimir los disparos restantes de cada jugador
def imprimir_disparos_restantes (disparos_restantes, jugador):
    print (f"Disparos restantes de {jugador}: {disparos_restantes}")
        

























