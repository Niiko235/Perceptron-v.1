from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def single_nube_2d(x, y, simbolo):
    plt.plot(x, y, simbolo)
    plt.show()




def doble_nube_2d(x1, y1, simbolo1, x2, y2, simbolo2):
    plt.plot(x1, y1, simbolo1) # .plot nos permite graficar puntos, lineas, etc. dependiendo del simbolo que le pasemos'
    plt.plot(x2, y2, simbolo2)
    plt.axis('equal') # para que los ejes tengan la misma escala - porporcion
    plt.show()


def doble_nube_3d(x1, y1, z1, x2, y2, z2, x_line, y_line, z_line):

    fig = plt.figure()

    # especificamos que queremos una grafica en 3D    
    ax = fig.add_subplot(111, projection='3d')

    # .scatter nos permite graficar puntos en 3D
    ax.scatter(x1, y1, z1, c='r') 
    ax.scatter(x2, y2, z2, c='b')

    # .plot nos permite graficar lineas en 3D
    ax.plot_surface(x_line, y_line, z_line)

    # mostrar la grafica 
    plt.show()