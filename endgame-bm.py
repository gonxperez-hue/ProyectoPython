#En esta parte solicitaremos la acción del jugador
opcion = input("Ingrese una de las tres opciones posible D para destapar, M para marcar U para desmarcar    : ")

#Procesamos la acción del jugador
if opcion == "D":
    #Solicitamos la fila y la columna a destapar
    fila = int(input("Ingrese la fila : "))
    columna = int(input("Ingrese la columna : "))

#Destapar la casilla
visible = [fila][columna] = True

#Si la casilla contiene una mina, el jugador pierde
if minas [fila][columna]:
    juego_en_curso = False
    print("Game over pare, a llorar a otro lado")

elif opcion == "M":
    #Solicitar la fila y columna a marcar
    fila = int(input("Ingrese la fila : "))
    columna = int(input("Ingrese la columna : "))

    #Marcar la casilla
    visible [fila][columna] = True
    minas [fila][columna] = True

elif opcion == "U":
    #Solicitar la fila y columna a desmarcar
    fila = int(input("Ingrese la fila : "))
    columna = int(input("Ingrese la columna : "))

    #Desmarcar la casilla
    visible [fila][columna] = False
    minas [fila][columna] = False



    
 








