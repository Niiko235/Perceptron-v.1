
import numpy as np 


def FuncionEscalon(h):
    return 1 if h >= 0 else 0


def perceptron2D(entradas, resultado_esperado, numero_puntos, pesos, bias, numero_epocas=10000, tasa_aprendizaje=0.01):
    """Vamos a implementar el algoritmo del perceptron para clasificar dos nubes de puntos en 2D, con una media diferente y una desviación estándar de 1."""

    epocas = []
    error = []

    for epoca in range(numero_epocas):
        for i in range(numero_puntos):
            # calculamos la salida del perceptron
            h = np.dot(pesos, entradas[i]) + bias

            # aplicamos la función de activación (en este caso, una función escalón)
            fh = FuncionEscalon(h)

            # calculamos el error
            error = resultado_esperado[i] - fh


            # Aprendizaje por iteración: actualizamos los pesos y el bias
            if error != 0:
                # Utilizamos la multiplicación escalar para actializar el vector de pesos directamente y no tener que actualizar cada peso por separado
                pesos = pesos + tasa_aprendizaje * error * entradas[i]
                bias = bias + tasa_aprendizaje * error
    

