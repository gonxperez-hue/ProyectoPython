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
# Estos métodos gestionan la lógica de colocación de barcos y disparos

class Tablero:
    """Continuación de la clase Tablero - Métodos de juego"""
    
    def puede_colocar_barco(self, fila, col, longitud, horizontal):
        """
        Verifica si se puede colocar un barco en una posición específica
        Comprueba que:
        1. No se salga del tablero
        2. No haya otro barco en las casillas
        3. No haya barcos adyacentes (diagonal incluida)
        
        Args:
            fila (int): Fila inicial
            col (int): Columna inicial
            longitud (int): Longitud del barco
            horizontal (bool): True si es horizontal, False si es vertical
        
        Returns:
            bool: True si se puede colocar, False si no
        """
        if horizontal:
            # Verificar que no se salga del tablero horizontalmente
            if col + longitud > self.tamaño:
                return False
            
            # Verificar espacio y casillas adyacentes (incluye diagonales)
            # Esto evita que los barcos se toquen
            for c in range(max(0, col - 1), min(self.tamaño, col + longitud + 1)):
                for r in range(max(0, fila - 1), min(self.tamaño, fila + 2)):
                    if self.cuadricula[r][c] == 'B':
                        return False
        else:
            # Verificar que no se salga del tablero verticalmente
            if fila + longitud > self.tamaño:
                return False
            
            # Verificar espacio y casillas adyacentes
            for r in range(max(0, fila - 1), min(self.tamaño, fila + longitud + 1)):
                for c in range(max(0, col - 1), min(self.tamaño, col + 2)):
                    if self.cuadricula[r][c] == 'B':
                        return False
        return True
    
    def colocar_barco(self, barco, fila, col, horizontal):
        """
        Coloca un barco en el tablero en la posición especificada
        Marca las casillas con 'B' y guarda las posiciones en el objeto barco
        
        Args:
            barco (Barco): Objeto barco a colocar
            fila (int): Fila inicial
            col (int): Columna inicial
            horizontal (bool): Orientación del barco
        
        Returns:
            bool: True si se colocó correctamente
        """
        posiciones = []













