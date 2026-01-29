from Tablero import tablero_vacio, hacer_tablero_visible, mostrar_tablero
from Minas import generar_minas, colocar_minas, calcular_numeros

def jugar():
    #Configuración
    f, c = 6, 6
    minas_totales = 5
    
    # Hemos usado Tablero.py para crear la estructura
    tablero_oculto = tablero_vacio(f, c)
    tablero_jugador = hacer_tablero_visible(f, c)
    
    # Usamos Minas.py para poner la lógica
    posiciones_minas = generar_minas(f, c, minas_totales)
    colocar_minas(tablero_oculto, posiciones_minas)
    calcular_numeros(tablero_oculto)
    
    #Esto muestra el juego ya directamente
    print("Buscaminas preparado")
    print("Tablero:")
    mostrar_tablero(tablero_jugador)
    
if __name__ == "__Buscaminas__":
    jugar()