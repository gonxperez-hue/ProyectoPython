import random
import os
import time

# CLASE BARCO

# Esta clase representa un barco individual en el juego
# Cada barco tiene un nombre, longitud, posiciones que ocupa e impactos recibidos

class Barco:
    """Representa un barco en el juego"""
    
    def __init__(self, nombre, longitud):
        """
        Constructor de la clase Barco
        
        Args:
            nombre: Nombre del barco (ej: "Portaaviones", "Submarino")
            longitud: Cantidad de casillas que ocupa el barco
        """
        self.nombre = nombre              # Nombre del barco
        self.longitud = longitud          # Tamaño del barco (número de casillas)
        self.posiciones = []              # Lista de coordenadas (fila, col) que ocupa
        self.impactos = 0                 # Contador de impactos recibidos

    def esta_hundido(self):
        """
        Verifica si el barco está completamente hundido
        Un barco está hundido cuando los impactos igualan su longitud en el tablero
        
        Returns:
            bool: True si está hundido, False si aún flota
        """
        return self.impactos >= self.longitud

# CLASE TABLERO - PARTE 1

# Esta clase gestiona el tablero de juego completo
# Incluye la cuadrícula, los barcos colocados y los disparos

class Tablero:
    """Representa el tablero de juego"""
    
    def __init__(self, tamaño=10):
        """
        Constructor del tablero
        
        Args:
            tamaño: Tamaño del tablero
        """
        self.tamaño = tamaño
        # Cuadrícula principal con '~' representando el agua
        self.cuadricula = [['~' for _ in range(tamaño)] for _ in range(tamaño)]
        self.barcos = []  # Lista de barcos colocados en este tablero
        # Cuadrícula para registrar disparos realizados
        self.disparos = [['~' for _ in range(tamaño)] for _ in range(tamaño)]

    def mostrar_tablero(self, ocultar_barcos=False):
        """
        Muestra el tablero en consola con formato visual
        
        Args:
            ocultar_barcos: Si True, oculta las posiciones de los barcos
                                   (usado para mostrar el tablero enemigo)
        
        Formato:
        - Letras (A-J) para columnas
        - Números (0-9) para filas
        - 'B' = Barco, 'X' = Tocado, 'O' = Agua, '~' = No explorado
        """
        # Mostrar letras de columnas (A, B, C, ...)
        print("\n   " + " ".join([chr(65 + i) for i in range(self.tamaño)]))
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
        
        # Mostrar cada fila con su número
        for i in range(self.tamaño):
            fila = f"{i:2}|"  # Número de fila con formato
            for j in range(self.tamaño):
                # Si se deben ocultar barcos y hay un barco, mostrar agua
                if ocultar_barcos and self.cuadricula[i][j] == 'B':
                    fila += "~ "
                else:
                    fila += self.cuadricula[i][j] + " "
            print(fila + "|")
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")

    def mostrar_disparos(self):
        """
        Muestra el tablero de disparos realizados
        Útil para que el jugador vea dónde ha disparado anteriormente
        
        Símbolos:
        - '~' = No disparado
        - 'X' = Impacto en barco
        - 'O' = Agua (fallo)
        """
        print("\n   " + " ".join([chr(65 + i) for i in range(self.tamaño)]))
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
        
        for i in range(self.tamaño):
            fila = f"{i:2}|"
            for j in range(self.tamaño):
                fila += self.disparos[i][j] + " "
            print(fila + "|")
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
