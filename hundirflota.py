import random
import os

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

# ============================================================================
# CLASE TABLERO - PARTE 2 (continuación)
# ============================================================================
# Métodos que controlan la colocación de barcos y los disparos

class Tablero:
    """Continuación de la clase Tablero - Métodos de juego"""
    
    def puede_colocar_barco(self, fila, col, longitud, horizontal):
        """
        Verifica si un barco puede colocarse en la posición indicada
        """
        if horizontal:
            # Evita que el barco salga del tablero horizontalmente
            if col + longitud > self.tamaño:
                return False
            
            # Revisa casillas ocupadas o adyacentes (incluye diagonales)
            for c in range(max(0, col - 1), min(self.tamaño, col + longitud + 1)):
                for r in range(max(0, fila - 1), min(self.tamaño, fila + 2)):
                    if self.cuadricula[r][c] == 'B':  # Detecta otro barco
                        return False
        else:
            # Evita que el barco salga del tablero verticalmente
            if fila + longitud > self.tamaño:
                return False
            
            # Revisa casillas ocupadas o adyacentes
            for r in range(max(0, fila - 1), min(self.tamaño, fila + longitud + 1)):
                for c in range(max(0, col - 1), min(self.tamaño, col + 2)):
                    if self.cuadricula[r][c] == 'B':  # Detecta otro barco
                        return False
        
        return True  # Todo correcto, se puede colocar
    
    def colocar_barco(self, barco, fila, col, horizontal):
        """
        Coloca un barco en el tablero y registra sus posiciones
        """
        posiciones = []  # Guarda las coordenadas del barco


        if horizontal:
            # Colocar barco horizontalmente (misma fila, columnas seguidas)
            for i in range(barco.longitud):
                self.cuadricula[fila][col + i] = 'B'   # Marca casilla como barco
                posiciones.append((fila, col + i))    # Guarda coordenada
        else:
            # Colocar barco verticalmente (misma columna, filas seguidas)
            for i in range(barco.longitud):
                self.cuadricula[fila + i][col] = 'B'  # Marca casilla como barco
                posiciones.append((fila + i, col))    # Guarda coordenada
        
        # Registrar posiciones en el objeto barco
        barco.posiciones = posiciones
        # Añadir barco a la lista del tablero
        self.barcos.append(barco)
        return True  # Colocación exitosa
    
    def colocar_barcos_aleatorio(self, lista_barcos):
        """
        Coloca todos los barcos de forma aleatoria en el tablero
        """
        for nombre, longitud in lista_barcos:
            barco = Barco(nombre, longitud)  # Crear barco
            colocado = False                 # Controla si se colocó
            intentos = 0                     # Contador de intentos

            # Intentar colocar el barco hasta 100 veces
            while not colocado and intentos < 100:
                # Generar posición aleatoria dentro del tablero
                fila = random.randint(0, self.tamaño - 1)
                col = random.randint(0, self.tamaño - 1)
                horizontal = random.choice([True, False])  # Orientación aleatoria
                
                # Si la posición es válida, colocar el barco
                if self.puede_colocar_barco(fila, col, longitud, horizontal):
                    self.colocar_barco(barco, fila, col, horizontal)
                    colocado = True  # Barco colocado con éxito
                
                intentos += 1  # Aumentar contador de intentos
    
    def recibir_disparo(self, fila, col):
        """
        Procesa un disparo en el tablero y actualiza el estado
        """
        if self.cuadricula[fila][col] == 'B':
            # Impacto directo: marcar casilla como tocada
            self.cuadricula[fila][col] = 'X'
            
        











