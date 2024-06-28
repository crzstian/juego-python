import random
import constantes
import pygame
import index
import random  

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
COLORES_BARCOS = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Azul para 2x1, Verde para 3x1, Rojo para 4x1

# Función para que un barco no quede encima de otro
def barco_se_superpone(barco_nuevo, lista_barcos):
    for barco in lista_barcos:
        for parte in barco:
            if parte in barco_nuevo:
                return barco_nuevo
    return False

# Función para barcos aleatorios
def generar_barcos_aleatorios(barcos_izquierda,barcos_derecha):
    barcos_izquierda.clear()
    barcos_derecha.clear()

    # Generar 3 barcos de 4x1 para cada lado
    for _ in range(3):
        while True:
            fila = random.randint(0, constantes.FILAS - 1)
            columna = random.randint(0, constantes.COLUMNAS - 4)
            barco = [(fila, columna + i) for i in range(4)]
            if not barco_se_superpone(barco, barcos_izquierda) and not barco_se_superpone(barco, barcos_derecha):
                break
        barcos_izquierda.append(barco)
        barcos_derecha.append(barco)

    # Generar 5 barcos de 3x1 para cada lado
    for _ in range(5):
        while True:
            fila = random.randint(0, constantes.FILAS - 1)
            columna = random.randint(0, constantes.COLUMNAS - 3)
            barco = [(fila, columna + i) for i in range(3)]
            if not barco_se_superpone(barco, barcos_izquierda) and not barco_se_superpone(barco, barcos_derecha):
                break
        barcos_izquierda.append(barco)
        barcos_derecha.append(barco)

    # Generar 4 barcos de 2x1 para cada lado
    for _ in range(4):
        while True:
            fila = random.randint(0, constantes.FILAS - 1)
            columna = random.randint(0, constantes.COLUMNAS - 2)
            barco = [(fila, columna + i) for i in range(2)]
            if not barco_se_superpone(barco, barcos_izquierda) and not barco_se_superpone(barco, barcos_derecha):
                break
        barcos_izquierda.append(barco)
        barcos_derecha.append(barco)

# Función para dibujar un tablero
def dibujar_tablero(ventana, x_offset, y_offset):
    for fila in range(constantes.FILAS):
        for columna in range(constantes.COLUMNAS):
            rect = pygame.Rect(x_offset + columna * constantes.ANCHO_CELDA, y_offset + fila * constantes.ALTO_CELDA, constantes.ANCHO_CELDA, constantes.ALTO_CELDA)
            pygame.draw.rect(ventana, NEGRO, rect, 1)

# Función para dibujar los barcos
def dibujar_barcos(ventana, x_offset, y_offset, lista_barcos):
    for barco in lista_barcos:
        # longitud del barco
        longitud_barco = len(barco)
        # Selecciona el color según la longitud del barco
        color = COLORES_BARCOS[longitud_barco - 2]  # Índice 0 para 2x1, 1 para 3x1, 2 para 4x1
        for parte in barco:
            fila, columna = parte
            rect = pygame.Rect(x_offset + columna * constantes.ANCHO_CELDA, y_offset + fila * constantes.ALTO_CELDA, constantes.ANCHO_CELDA, constantes.ALTO_CELDA)
            pygame.draw.rect(ventana, color, rect)

# Función para dibujar el botón "X" de cierre
def dibujar_boton_cerrar(ventana):
    pygame.draw.line(ventana, NEGRO, (index.ANCHO_VENTANA - 30, 10), (index.ANCHO_VENTANA - 10, 30), 2)
    pygame.draw.line(ventana, NEGRO, (index.ANCHO_VENTANA - 30, 30), (index.ANCHO_VENTANA - 10, 10), 2)
