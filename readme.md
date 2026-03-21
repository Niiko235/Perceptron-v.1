# Comando basicos

````
python3 archivo -> correr 
````


# Problema a desarrollar: Clasificacion de puntos en 2D y 3D
Este repositorio tiene como objetivo explicar y demostrar de forma pedagogica como funciona el perceptron y que se debe tener en mente a la hora de emplear uno. Este proyecto tiene como objetivo clasificar datos en dos clases, especificamente, se trabaja con nubes de puntos en dos dimensiones, que posteriormente se extediente a tres dimensiones; se busca explicar por qué el perceptron es la herramienta indicada para este problema, siempre y cuando las grupos de puntos sean linealmente separables.

## Objetivos
	•	Implementar un perceptrón binario sin librerías de machine learning.
	•	Clasificar dos nubes de puntos en 2D mediante una recta.
	•	Extender el modelo a 3 entradas (3D), donde la frontera de decisión es un plano.
	•	Analizar el comportamiento y limitaciones del modelo.
    •   Mostrar visualmente los resultados mediante Unity



# Fundamentos Teoricos
## ¿Que es un perceptron?
El perceptron es la unidad fundamental y mas simple dentro de la inteligencia artificial, funciona como una unica "neurona" y se caracteriza por ser un clasificador binario. Es decir, solo puede diferenciar entre dos cosas. Funciona bajo el aprendizaje de maquina supervisado, requiere de datos base para entrenarse en el contexto en la que requeramos usarla.

Es uno de los modelos más simples dentro del aprendizaje automático y constituye la base de las redes neuronales.

## Partes de un perceptron 
### Entradas 
### Pesos
### Sesgo / Bias
### Salida
## ¿En que consiste el trabajo del perceptron?
Desde la explicación matematica, El perceptrón calcula una combinación lineal de las entradas:
	•	x_i: entradas
	•	w_i: pesos
	•	b: sesgo (bias)
	•	f: función de activación

