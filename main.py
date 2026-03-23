import numpy as np



def perceptron_3d_2Nubes(numero_puntos=100):
    
    # importamos las funciones que necesitamos para generar los datos y graficarlos
    from generarDatos import generar_datos_3d_2Nubes
    from perceptron import perceptron_3d_2Nubes
    from graficas import doble_nube_3d


    # generamos los datos 
    x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2 , resultado_esperado = generar_datos_3d_2Nubes(numero_puntos)


    entradas = np.vstack((np.column_stack((x_nube1, y_nube1, z_nube1)), np.column_stack((x_nube2, y_nube2, z_nube2))))

    # pesos y bias
    pesos = np.random.rand(3)
    bias = 1

    pesos, bias = perceptron_3d_2Nubes(entradas, resultado_esperado, numero_puntos*2, pesos, bias, numero_epocas=1000, tasa_aprendizaje=0.0001)

    #x_line = np.linspace(-8, 8, 100)
    ##x_line, y_line = np.meshgrid(x_line, y_line)

    #z_line = -(pesos[0] * x_line + pesos[1] * y_line + bias) / pesos[2]

    #doble_nube_3d(x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2, x_line, y_line, z_line)



perceptron_3d_2Nubes(100)