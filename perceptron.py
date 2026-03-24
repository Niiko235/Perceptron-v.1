
import numpy as np
from exportData import export_2nubes_3d
from exportData import export_epocas_2nubes_3d

def funcion_escalon(h):
    return 1 if h >= 0 else 0

def perceptron2D(entradas, resultado_esperado, numero_puntos, pesos, bias, numero_epocas=100, tasa_aprendizaje=0.01):
    """Vamos a implementar el algoritmo del perceptron para clasificar dos nubes de puntos en 2D, con una media diferente y una desviación estándar de 1."""

    epocas = []
    error = []

    for epoca in range(numero_epocas):
        for i in range(numero_puntos):
            # calculamos la salida del perceptron
            h = np.dot(pesos, entradas[i]) + bias

            # aplicamos la función de activación (en este caso, una función escalón)
            fh = funcion_escalon(h)

            # calculamos el error
            error = resultado_esperado[i] - fh


            # Aprendizaje por iteración: actualizamos los pesos y el bias
            if error != 0:
                # Utilizamos la multiplicación escalar para actializar el vector de pesos directamente y no tener que actualizar cada peso por separado
                pesos = pesos + tasa_aprendizaje * error * entradas[i]
                bias = bias + tasa_aprendizaje * error


def perceptron_3d_2Nubes(entradas, resultado_esperado, numero_puntos, pesos, bias, numero_epocas=100, tasa_aprendizaje=0.01):
    """Entrenamos el perceptron con el algoritmo de aprendizaje supervisado, para que aprenda a clasificar las nubes de puntos en 3D"""
    errores = []
    w = []
    b = []

    print(f'pesos al iniciar el entrenamiento: {pesos}')
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
        # print(f'Epoca {epoca+1}/{numero_epocas}, Errores: {num_errores}')
        print(f'pesos al finalizar la epoca {epoca+1}: {pesos}, bias: {bias}')
        error = num_errores / numero_puntos
        errores.append(error)
        w.append(pesos.copy())
        b.append(bias)

    export_2nubes_3d(entradas, resultado_esperado)
    export_epocas_2nubes_3d(errores, w, b)

    
    return pesos, bias



def perceptron_3d_3Nubes(entradas, resultado_esperado, numero_puntos, pesos, bias, numero_epocas=100, tasa_aprendizaje=0.01):
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
        # print(f'Epoca {epoca+1}/{numero_epocas}, Errores: {num_errores}')
       
        error = num_errores / numero_puntos
        errores.append(error)
        w.append(pesos.copy())
        b.append(bias)
    
    return pesos, bias, errores, w, b