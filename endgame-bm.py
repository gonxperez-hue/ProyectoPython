#Si el juego ha terminado, mostrar el tablero con las minas descubiertas
if juego_en_curso:
    print("Ganaste, Enhorabuena!")
    for i in range(filas):
        for j in range(columnas):
            if minas[i][j]:
                print ("*", end = " ")
            else:
                print (visible[i][j], end = " ")
           
            #ESTE PRINT ESTA MAL UBICADO, AHORA MISMO ESTA HACIENDO UN SALTO DE LINEA POR CADA CELDA
            print()    

            