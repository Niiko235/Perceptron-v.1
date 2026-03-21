import matplotlib.pyplot as plt



def single_nube_2d(x, y, simbolo):
    plt.plot(x, y, simbolo)
    plt.show()




def doble_nube_2d(x1, y1, simbolo1, x2, y2, simbolo2):
    plt.plot(x1, y1, simbolo1) # .plot nos permite graficar puntos, lineas, etc. dependiendo del simbolo que le pasemos'
    plt.plot(x2, y2, simbolo2)
    plt.axis('equal') # para que los ejes tengan la misma escala - porporcion
    plt.show()