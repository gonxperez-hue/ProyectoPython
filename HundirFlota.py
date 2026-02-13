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