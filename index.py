import pygame
import sys
import funcionesjuego
import constantes

pygame.init()

# Lista para barco en cada lado
barcos_izquierda = []
barcos_derecha = []

# Genera los barcos aleatorios
funcionesjuego.generar_barcos_aleatorios(barcos_izquierda,barcos_derecha)

ANCHO_VENTANA = 2 * (constantes.COLUMNAS * constantes.ANCHO_CELDA) + constantes.SEPARACION + 2 * constantes.MARGEN
ALTO_VENTANA = constantes.FILAS * constantes.ALTO_CELDA + 2 * constantes.MARGEN

# Crea la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tablero con Barcos")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
COLORES_BARCOS = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Azul para 2x1, Verde para 3x1, Rojo para 4x1

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Verifica si se hizo clic en el botón "X" para cerrar la ventana
            if ANCHO_VENTANA - 30 <= evento.pos[0] <= ANCHO_VENTANA - 10 and 10 <= evento.pos[1] <= 30:
                pygame.quit()
                sys.exit()

    # Dibuja el fondo de la ventana
    ventana.fill(BLANCO)
    
    # Dibuja el primer tablero con margen para la izquierda
    funcionesjuego.dibujar_tablero(ventana, constantes.MARGEN, constantes.MARGEN)
    funcionesjuego.dibujar_barcos(ventana, constantes.MARGEN, constantes.MARGEN, barcos_izquierda)
    
    # Dibuja el segundo tablero con margen y separación para la derecha
    funcionesjuego.dibujar_tablero(ventana, constantes.MARGEN + constantes.COLUMNAS * constantes.ANCHO_CELDA + constantes.SEPARACION, constantes.MARGEN)
    funcionesjuego.dibujar_barcos(ventana, constantes.MARGEN + constantes.COLUMNAS * constantes.ANCHO_CELDA + constantes.SEPARACION, constantes.MARGEN, barcos_derecha)
    
    # Dibuja el botón "X" para cerrar la ventana
    funcionesjuego.dibujar_boton_cerrar(ventana)
    
    # Actualiza la pantalla
    pygame.display.flip()
