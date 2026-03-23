
import numpy as np
from exportData import export_2nubes_3d
from exportData import export_epocas_2nubes_3d

def funcion_escalon(h):
    return 1 if h >= 0 else 0


def perceptron_3d_2Nubes(entradas, resultado_esperado, numero_puntos, pesos, bias, numero_epocas=100, tasa_aprendizaje=0.01):
    """Entrenamos el perceptron con el algoritmo de aprendizaje supervisado, para que aprenda a clasificar las nubes de puntos en 3D"""
    errores = []
    w = []
    b = []

    for epoca in range(numero_epocas):
        num_errores = 0
        for i in range(numero_puntos):
            # calculamos la salida del perceptron
            h = np.dot(pesos, entradas[i]) + bias

            #funcion de activacion
            fh = funcion_escalon(h)

            # calculamos el error
            error = resultado_esperado[i] - fh

            # Entrenamiento 
            if error != 0:
                num_errores += 1
                pesos += tasa_aprendizaje * error * entradas[i]
                bias += tasa_aprendizaje * error
        print(f'Epoca {epoca+1}/{numero_epocas}, Errores: {num_errores}')
        error = num_errores / numero_puntos
        errores.append(error)
        w.append(pesos.copy())
        b.append(bias)

    export_2nubes_3d(entradas, resultado_esperado)
    export_epocas_2nubes_3d(errores, w, b)

    
    return pesos, bias