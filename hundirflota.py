import random
import os
import time

# ============================================================================
# PARTE DE HUGO: CLASE BARCO
# ============================================================================
class Barco:
    """Representa un barco en el juego"""
    
    def __init__(self, nombre, longitud):
        self.nombre = nombre              # Nombre del barco
        self.longitud = longitud          # Tamaño del barco (número de casillas)
        self.posiciones = []              # Lista de coordenadas (fila, col) que ocupa
        self.impactos = 0                 # Contador de impactos recibidos
    
    def esta_hundido(self):
        """Verifica si el barco está completamente hundido"""
        return self.impactos >= self.longitud


# ============================================================================
# PARTE DE HUGO Y Abelardo: CLASE TABLERO FUSIONADA
# ============================================================================
class Tablero:
    """Representa el tablero de juego"""
    
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        # Cuadrícula principal con '~' representando agua
        self.cuadricula = [['~' for _ in range(tamaño)] for _ in range(tamaño)]
        self.barcos = []  # Lista de barcos colocados en este tablero
        # Cuadrícula para registrar disparos realizados
        self.disparos = [['~' for _ in range(tamaño)] for _ in range(tamaño)]
    
    # --- Métodos de Visualización (Hugo) ---
    def mostrar_tablero(self, ocultar_barcos=False):
        print("\n   " + " ".join([chr(65 + i) for i in range(self.tamaño)]))
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
        for i in range(self.tamaño):
            fila = f"{i:2}|"
            for j in range(self.tamaño):
                if ocultar_barcos and self.cuadricula[i][j] == 'B':
                    fila += "~ "
                else:
                    fila += self.cuadricula[i][j] + " "
            print(fila + "|")
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
    
    def mostrar_disparos(self):
        print("\n   " + " ".join([chr(65 + i) for i in range(self.tamaño)]))
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")
        for i in range(self.tamaño):
            fila = f"{i:2}|"
            for j in range(self.tamaño):
                fila += self.disparos[i][j] + " "
            print(fila + "|")
        print("  +" + "-" * (self.tamaño * 2 - 1) + "+")

    # --- Métodos de Lógica (Abelardo) ---
    def puede_colocar_barco(self, fila, col, longitud, horizontal):
        if horizontal:
            if col + longitud > self.tamaño:
                return False
            for c in range(max(0, col - 1), min(self.tamaño, col + longitud + 1)):
                for r in range(max(0, fila - 1), min(self.tamaño, fila + 2)):
                    if self.cuadricula[r][c] == 'B':
                        return False
        else:
            if fila + longitud > self.tamaño:
                return False
            for r in range(max(0, fila - 1), min(self.tamaño, fila + longitud + 1)):
                for c in range(max(0, col - 1), min(self.tamaño, col + 2)):
                    if self.cuadricula[r][c] == 'B':
                        return False
        return True
    
    def colocar_barco(self, barco, fila, col, horizontal):
        posiciones = []
        if horizontal:
            for i in range(barco.longitud):
                self.cuadricula[fila][col + i] = 'B'
                posiciones.append((fila, col + i))
        else:
            for i in range(barco.longitud):
                self.cuadricula[fila + i][col] = 'B'
                posiciones.append((fila + i, col))
        
        barco.posiciones = posiciones
        self.barcos.append(barco)
        return True
    
    def colocar_barcos_aleatorio(self, lista_barcos):
        for nombre, longitud in lista_barcos:
            barco = Barco(nombre, longitud)
            colocado = False
            intentos = 0
            while not colocado and intentos < 100:
                fila = random.randint(0, self.tamaño - 1)
                col = random.randint(0, self.tamaño - 1)
                horizontal = random.choice([True, False])
                if self.puede_colocar_barco(fila, col, longitud, horizontal):
                    self.colocar_barco(barco, fila, col, horizontal)
                    colocado = True
                intentos += 1
    
    def recibir_disparo(self, fila, col):
        if self.cuadricula[fila][col] == 'B':
            self.cuadricula[fila][col] = 'X'
            for barco in self.barcos:
                if (fila, col) in barco.posiciones:
                    barco.impactos += 1
                    if barco.esta_hundido():
                        return "hundido", barco.nombre
                    return "tocado", None
        elif self.cuadricula[fila][col] == '~':
            self.cuadricula[fila][col] = 'O'
            return "agua", None
        else:
            return "repetido", None
    
    def todos_hundidos(self):
        return all(barco.esta_hundido() for barco in self.barcos)


# ============================================================================
# PARTE DE Pablo: CLASE PRINCIPAL DEL JUEGO
# ============================================================================
class JuegoHundirFlota:
    """Clase principal del juego Hundir la Flota"""
    
    def __init__(self):
        self.tamaño_tablero = 10
        self.barcos = [
            ("Portaaviones", 5),
            ("Acorazado", 4),
            ("Crucero", 3),
            ("Submarino", 3),
            ("Destructor", 2)
        ]
        self.tablero_jugador = Tablero(self.tamaño_tablero)
        self.tablero_cpu = Tablero(self.tamaño_tablero)
        
        self.disparos_cpu = []
        self.ultimo_impacto_cpu = None
        self.modo_caza_cpu = []
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_estado_juego(self):
        self.limpiar_pantalla()
        print("=" * 50)
        print("       HUNDIR LA FLOTA - BATTLESHIP")
        print("=" * 50)
        print("\n        TU TABLERO")
        self.tablero_jugador.mostrar_tablero(ocultar_barcos=False)
        print("\n     TUS DISPAROS (Tablero Enemigo)")
        self.tablero_jugador.mostrar_disparos()
        print("\nLeyenda: ~ Agua | B Barco | X Tocado | O Fallo")
    
    def obtener_coordenadas(self):
        while True:
            try:
                entrada = input("\nIngresa coordenadas (ej: A5, B3): ").strip().upper()
                if len(entrada) < 2:
                    print("Coordenadas inválidas. Intenta de nuevo.")
                    continue
                col = ord(entrada[0]) - 65
                fila = int(entrada[1:])
                if 0 <= fila < self.tamaño_tablero and 0 <= col < self.tamaño_tablero:
                    return fila, col
                else:
                    print(f"Coordenadas fuera del tablero. Usa A-{chr(64 + self.tamaño_tablero)} y 0-{self.tamaño_tablero - 1}")
            except (ValueError, IndexError):
                print("Formato inválido. Usa letra + número (ej: A5)")
    
    def turno_jugador(self):
        self.mostrar_estado_juego()
        print("\n--- TU TURNO ---")
        while True:
            fila, col = self.obtener_coordenadas()
            if self.tablero_jugador.disparos[fila][col] != '~':
                print("Ya disparaste en esa posición. Intenta otra.")
                continue
            resultado, barco_nombre = self.tablero_cpu.recibir_disparo(fila, col)
            if resultado == "tocado":
                self.tablero_jugador.disparos[fila][col] = 'X'
                print("\n¡TOCADO! 🎯")
            elif resultado == "hundido":
                self.tablero_jugador.disparos[fila][col] = 'X'
                print(f"\n¡HUNDIDO! ⚓ Has hundido el {barco_nombre}")
            elif resultado == "agua":
                self.tablero_jugador.disparos[fila][col] = 'O'
                print("\nAgua... 💧")
            time.sleep(2)
            break
    
    def turno_cpu(self):
        print("\n--- TURNO DE LA COMPUTADORA ---")
        time.sleep(1)
        if self.modo_caza_cpu:
            fila, col = self.modo_caza_cpu.pop(0)
        else:
            while True:
                fila = random.randint(0, self.tamaño_tablero - 1)
                col = random.randint(0, self.tamaño_tablero - 1)
                if (fila, col) not in self.disparos_cpu:
                    break
        
        self.disparos_cpu.append((fila, col))
        resultado, barco_nombre = self.tablero_jugador.recibir_disparo(fila, col)
        coord_str = f"{chr(65 + col)}{fila}"
        
        if resultado == "tocado":
            print(f"La CPU disparó en {coord_str}: ¡TOCADO! 💥")
            self.ultimo_impacto_cpu = (fila, col)
            for df, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nf, nc = fila + df, col + dc
                if (0 <= nf < self.tamaño_tablero and 0 <= nc < self.tamaño_tablero and (nf, nc) not in self.disparos_cpu):
                    self.modo_caza_cpu.append((nf, nc))
        elif resultado == "hundido":
            print(f"La CPU disparó en {coord_str}: ¡HUNDIÓ tu {barco_nombre}! ⚓")
            self.ultimo_impacto_cpu = None
            self.modo_caza_cpu = []
        elif resultado == "agua":
            print(f"La CPU disparó en {coord_str}: Agua")
        time.sleep(2)
    
    def jugar(self):
        self.limpiar_pantalla()
        print("=" * 50)
        print("       BIENVENIDO A HUNDIR LA FLOTA")
        print("=" * 50)
        print("\nColocando barcos...")
        
        self.tablero_jugador.colocar_barcos_aleatorio(self.barcos)
        self.tablero_cpu.colocar_barcos_aleatorio(self.barcos)
        
        print("\n¡Barcos colocados! El juego comienza...\n")
        time.sleep(2)
        
        while True:
            self.turno_jugador()
            if self.tablero_cpu.todos_hundidos():
                self.mostrar_estado_juego()
                print("\n" + "=" * 50)
                print("     ¡FELICIDADES! ¡HAS GANADO! 🏆")
                print("=" * 50)
                break
            
            self.turno_cpu()
            if self.tablero_jugador.todos_hundidos():
                self.mostrar_estado_juego()
                print("\n" + "=" * 50)
                print("     LA COMPUTADORA HA GANADO 😢")
                print("=" * 50)
                break

# ============================================================================
# ARRANQUE DEL JUEGO
# ============================================================================
if __name__ == "__main__":
    juego = JuegoHundirFlota()
    juego.jugar()
















