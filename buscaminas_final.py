# Juego.py
from Tablero_buscaminas import tablero_vacio, hacer_tablero_visible, mostrar_tablero, destapar, marcar, desmarcar
from Minas import generar_minas, colocar_minas, calcular_numeros

def jugar():
    filas, columnas = 6, 6
    minas_totales = 5

    tablero_oculto = tablero_vacio(filas, columnas)
    tablero_jugador = hacer_tablero_visible(filas, columnas)

    posiciones_minas = generar_minas(filas, columnas, minas_totales)
    colocar_minas(tablero_oculto, posiciones_minas)
    calcular_numeros(tablero_oculto)

    juego_en_curso = True

    print("= BUSCAMINAS =")
    mostrar_tablero(tablero_jugador)

    while juego_en_curso:
        opcion = input("D = destapar | M = marcar | U = desmarcar: ").upper()

        if opcion not in ["D", "M", "U"]:
            print("Opción inválida.")
            continue

        f = int(input("Fila: "))
        c = int(input("Columna: "))

        if opcion == "D":
            if tablero_oculto[f][c] == "M":
                print("Has perdido.")
                juego_en_curso = False
                break
            destapar(tablero_jugador, tablero_oculto, f, c)

        elif opcion == "M":
            marcar(tablero_jugador, f, c)

        elif opcion == "U":
            desmarcar(tablero_jugador, f, c)

        mostrar_tablero(tablero_jugador)

        # Comprobar victoria
        descubiertas = sum(
            1 for i in range(filas) for j in range(columnas)
            if tablero_jugador[i][j] != "." and tablero_jugador[i][j] != "F"
        )

        if descubiertas == filas * columnas - minas_totales:
            print("¡Has ganado!")
            juego_en_curso = False

    print("\nTablero final:")
    mostrar_tablero(tablero_oculto)

if __name__ == "__main__":
    jugar()
