import numpy as np


def export_2nubes_3d(entradas, resultado_esperado):

    data = np.column_stack((entradas, resultado_esperado))

    np.savetxt( './datosExportados/entradas_3d_2nubes.csv', data, delimiter=',', header='x,y,z,resultado_esperado', comments='')



def export_epocas_2nubes_3d(error, pesos, bias):

    data = np.column_stack((error, pesos, bias))

    np.savetxt( './datosExportados/epocas_3d_2nubes.csv', data, delimiter=',', header='error,peso1,peso2,peso3,bias', comments='')







def export_3nubes_3d(entradas, resultado_esperado1,resultado_esperado2):

    data = np.column_stack((entradas, resultado_esperado1, resultado_esperado2))

    np.savetxt( './datosExportados/entradas_3d_3nubes.csv', data, delimiter=',', header='x,y,z,resultado_esperado1,resultado_esperado2', comments='')


def export_epocas_3nubes_3d(error, pesos, bias, nombre):

    data = np.column_stack((error, pesos, bias))

    np.savetxt( f'./datosExportados/{nombre}.csv', data, delimiter=',', header='error,peso1,peso2,peso3,bias', comments='')