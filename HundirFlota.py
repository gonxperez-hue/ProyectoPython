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