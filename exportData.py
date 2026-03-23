import numpy as np


def export_2nubes_3d(entradas, resultado_esperado):

    data = np.column_stack((entradas, resultado_esperado))

    np.savetxt( './datosExportados/entradas_3d_2nubes.csv', data, delimiter=',', header='x,y,z,resultado_esperado', comments='')



def export_epocas_2nubes_3d(error, pesos, bias):

    data = np.column_stack((error, pesos, bias))

    np.savetxt( './datosExportados/epocas_3d_2nubes.csv', data, delimiter=',', header='error,peso1,peso2,peso3,bias', comments='')