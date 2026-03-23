import numpy as np



def generar_datos_2d_2Nubes():
    """Vamos a generar dos nubes de puntos en 2D, cada una con 100 particulas, con una media diferente y una desviación estándar de 1."""


    # Para crear la nube de puntos utilizamos la funcion normal de distribuion, multivariate_normal, que nos permite generar conjuntos de datos de 2d, 3d, etc. con una media y una desviación estándar especifica.
    # primer parametro: la media - centro de la nube, al ser 2d le pasamos el x y
    # segundo parametro covarianza:  
    # tercer parametro: el numero de puntos a genera
    # T: nos da las transpuesta de la matriz, para que nos de dos arrays, uno con las coordenadas x y otro con las coordenadas y
    x_nube1, y_nube1 = np.random.multivariate_normal(mean=[-2, -2], cov=[[1, -0.3], [-0.3, 1]], size=100).T

    return x_nube1, y_nube1


def generar_datos_3d_2Nubes(numero_puntos=100):
    """Vamos a generar una nube de puntos en 2D, con una media diferente y una desviación estándar de 1."""

    x_nube1, y_nube1, z_nube1 = np.random.multivariate_normal(mean=[-3, -3, -3], cov=[[1, -0.3, 1], [-0.3, 1, 1], [1, 1, -0.3]], size=numero_puntos).T

    x_nube2, y_nube2, z_nube2 = np.random.multivariate_normal(mean=[3, 3, 3], cov=[[1, -0.3, 1], [-0.3, 1, 1], [1, 1, -0.3]], size=numero_puntos).T

    return x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2, np.array([0]*numero_puntos + [1]*numero_puntos)