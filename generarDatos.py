import numpy as np


def generar_datos_3d_2Nubes(numero_puntos=100):
    """Vamos a generar una nube de puntos en 2D, con una media diferente y una desviación estándar de 1."""

    x_nube1, y_nube1, z_nube1 = np.random.multivariate_normal(mean=[-3, -3, -3], cov=[[1, -0.3, 1], [-0.3, 1, 1], [1, 1, -0.3]], size=numero_puntos).T

    x_nube2, y_nube2, z_nube2 = np.random.multivariate_normal(mean=[3, 3, 3], cov=[[1, -0.3, 1], [-0.3, 1, 1], [1, 1, -0.3]], size=numero_puntos).T

    return x_nube1, y_nube1, z_nube1, x_nube2, y_nube2, z_nube2, np.array([0]*numero_puntos + [1]*numero_puntos)