import numpy as np


def perceptron_2d_2Nubes(numero_puntos=100):
    
    # importamos las funciones que necesitamos para generar los datos y graficarlos
    from generarDatos import generar_datos_2d_2Nubes
    from graficas import doble_nube_2d
    from perceptron import perceptron2D

    # generamos los datos 
    x_nube1, y_nube1, x_nube2, y_nube2 , resultado_esperado = generar_datos_2d_2Nubes(numero_puntos)

    entradas = np.vstack((np.column_stack((x_nube1, y_nube1)), np.column_stack((x_nube2, y_nube2))))

    # Pesos y Bias
    pesos = np.ones(2) # 2 pesos para las 2 entradas
    bias = 0


    # perceptron2D
    perceptron2D(entradas, resultado_esperado, numero_puntos*2, pesos, bias, numero_epocas=100, tasa_aprendizaje=0.01)


    # graficamos las nubes de puntos y su recta para ver si el entramiento fue efectivo

    # generamos 100 puntos entre -6 y 6 para graficar la recta de decision
    x_line = np.linspace(-6, 6, 100) 
    # Sabemos que el perceptron satisface 
    y_line = -(pesos[0]*x_line + bias)/pesos[1] 

    doble_nube_2d(x_nube1, y_nube1, 'ro', x_nube2, y_nube2, 'bo', x_line, y_line)




perceptron_2d_2Nubes(200)



    