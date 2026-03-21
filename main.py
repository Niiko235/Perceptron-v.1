from generarDatos import generar_datos_2d_2Nubes

from graficas import single_nube_2d


x_nube1, y_nube1 = generar_datos_2d_2Nubes()

print(x_nube1)
print(y_nube1)

single_nube_2d(x_nube1, y_nube1, 'ro')




