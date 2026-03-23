import matplotlib.pyplot as plt



def single_nube_2d(x, y, simbolo):
    plt.plot(x, y, simbolo)
    plt.show()




def doble_nube_2d(x1, y1, simbolo1, x2, y2, simbolo2, x_line, y_line):
     
    # .plot nos permite graficar puntos, lineas, etc. dependiendo del simbolo que le pasemos'
    plt.plot(x1, y1, simbolo1)
    plt.plot(x2, y2, simbolo2)


    # graficamos la recta de decision del perceptron
    plt.plot(x_line, y_line)

    # para que los ejes tengan la misma escala - porporcion
    plt.axis('equal') 
    
    # Mostrar la grafica
    plt.show()
