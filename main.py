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


def perceptron_3d_2Nubes(numero_puntos=100):
    
    # importamos las funciones que necesitamos para generar los datos y graficarlos
    from generarDatos import generar_datos_3d_2Nubes
    from perceptron import perceptron_3d_2Nubes
    from graficas import doble_nube_3d


    # generamos los datos 
    x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2 , resultado_esperado = generar_datos_3d_2Nubes(numero_puntos)


    entradas = np.vstack((np.column_stack((x_nube1, y_nube1, z_nube1)), np.column_stack((x_nube2, y_nube2, z_nube2))))

    # pesos y bias
    pesos = np.ones(3)
    print(f'pesos antes de entrar al perceptron: {pesos}')
    bias = 1

    pesos, bias = perceptron_3d_2Nubes(entradas, resultado_esperado, numero_puntos*2, pesos, bias, numero_epocas=80, tasa_aprendizaje=0.01)

    

    u = np.linspace(-2, 12, 100)
    v = np.linspace(-2, 12, 100)
    u, v = np.meshgrid(u, v)

    x_line, y_line = u, v
    z_line = -(pesos[0] * x_line + pesos[1] * y_line + bias) / pesos[2]

   

    doble_nube_3d(x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2, x_line, y_line, z_line)




def perceptron_3d_3Nubes(numero_puntos=100):
    
    # importamos las funciones que necesitamos para generar los datos y graficarlos
    from generarDatos import generar_datos_3d_3Nubes
    from perceptron import perceptron_3d_3Nubes
    from graficas import doble_nube_3d
    from exportData import export_3nubes_3d, export_epocas_3nubes_3d


    # generamos los datos 
    x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2 , x_nube3, y_nube3, z_nube3, resultado_esperado1, resultado_esperado2 = generar_datos_3d_3Nubes(numero_puntos)


    entradas = np.vstack((np.column_stack((x_nube1, y_nube1, z_nube1)), np.column_stack((x_nube2, y_nube2, z_nube2)), np.column_stack((x_nube3, y_nube3, z_nube3))))

    # pesos y bias
    pesos1 = np.ones(3)
    bias1 = 0
    
    pesos2 = np.ones(3)
    bias2 = 0



    pesos1, bias1, listErrores1, listPesos1, listBias1  = perceptron_3d_3Nubes(entradas, resultado_esperado1, numero_puntos*3, pesos1, bias1, numero_epocas=250, tasa_aprendizaje=0.01)




    pesos2, bias2, listErrores2, listPesos2, listBias2 = perceptron_3d_3Nubes(entradas[100:], resultado_esperado2[100:], numero_puntos*2, pesos2, bias2, numero_epocas=250, tasa_aprendizaje=0.01)


    export_3nubes_3d(entradas, resultado_esperado1, resultado_esperado2)
    export_epocas_3nubes_3d(listErrores1, listPesos1, listBias1, 'epocas_3d_3nubes_clase1')
    export_epocas_3nubes_3d(listErrores2, listPesos2, listBias2, 'epocas_3d_3nubes_clase2')



perceptron_3d_3Nubes(100)