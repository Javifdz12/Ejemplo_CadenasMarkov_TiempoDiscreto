import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Queremos modelar el comportamiento de una persona que se mueve entre tres estados:
"casa", "trabajo" y "ocio". En un día cualquiera, la persona puede estar en uno de estos estados
y después de cada hora puede moverse a un estado diferente con cierta probabilidad.
Por ejemplo, si la persona está en casa, puede decidir ir al trabajo con una probabilidad del 50%,
ir al ocio con una probabilidad del 30% o quedarse en casa con una probabilidad del 20%.
Para implementar este modelo en Python, necesitamos definir la matriz de transición que describe
las probabilidades de transición entre los diferentes estados. La matriz de transición es una matriz cuadrada
en la que cada entrada indica la probabilidad de pasar de un estado a otro estado en una hora.
La matriz de transición para nuestro ejemplo se vería así:"""

# Definir la matriz de transición
P = np.array(
    [[0.2, 0.5, 0.3],
    [0.4, 0.1, 0.5],
    [0.2, 0.5, 0.3]])

"""En este caso, la entrada (i, j) de la matriz de transición P indica la probabilidad de pasar del estado i al estado j
en una hora. Por ejemplo, P[0, 1] = 0.5 indica que la probabilidad de pasar del estado "casa" al estado "trabajo" en una hora es del 50%.
Una vez que hemos definido la matriz de transición, podemos utilizarla para hacer una predicción del comportamiento futuro de la persona. 
Para hacer esto, necesitamos un vector inicial que describe la probabilidad de que la persona esté en cada estado al inicio del día. 
Por ejemplo, si sabemos que la persona suele pasar la mayor parte del tiempo en casa, podríamos definir el vector inicial de la siguiente manera:"""

# Definir el vector inicial
x0 = np.array([0.7, 0.2, 0.1])

"""En este caso, x0 es un vector columna en el que la entrada i indica la probabilidad de que la persona esté en el estado i al inicio del día. 
En este ejemplo, asumimos que la persona tiene una probabilidad del 70% de estar en casa al inicio del día, una probabilidad del 20% de estar en el trabajo 
y una probabilidad del 10% de estar en el ocio.
Para hacer una predicción del comportamiento futuro de la persona, simplemente tenemos que multiplicar
la matriz de transición P elevada a n(siendo n el instante futuro en el que quieres calcular las probailididades) por el vector inicial.
Esto nos da un nuevo vector que describe la probabilidad de que la persona esté en cada estado después de n horas:"""

# Calcular la distribución después de una hora
print("\n----Distribución después de una hora----\n")
x1 = np.dot(x0,P)
print(x1)

"""Si no se dispone de información previa sobre las probabilidades iniciales, se podría considerar una distribución uniforme que asigne la misma probabilidad a cada estado.
Por ejemplo, si la cadena de Markov tiene 3 estados, el vector inicial x0 se podría definir como:"""

# Definir el número de estados de la cadena
n = P.shape[0]

# Definir el vector inicial con distribución uniforme
x00 = np.full((1,n), 1/n)[0]


"""Las probabilidades de transición Pij en una cadena de Markov se determinan a partir del modelo que se está utilizando para describir el proceso estocástico que se está modelando.
En general, las probabilidades de transición se determinan a partir de datos históricos o del conocimiento experto sobre el sistema que se está modelando.
Por ejemplo, si estamos modelando el comportamiento de un sistema físico, las probabilidades de transición podrían ser obtenidas a partir de mediciones experimentales o simulaciones numéricas.
En algunos casos, las probabilidades de transición se pueden estimar a partir de datos de conteo, es decir, contando cuántas veces se ha observado una transición particular entre dos estados en el pasado. 
Si se dispone de un número suficiente de datos, se puede utilizar la frecuencia de ocurrencia de cada transición para estimar la probabilidad de transición correspondiente.
Es importante tener en cuenta que las probabilidades de transición en una cadena de Markov deben sumar 1 para cada fila de la matriz de transición P,
ya que la cadena debe pasar a un nuevo estado en cada paso de tiempo. Además, las probabilidades deben ser no negativas, ya que no es posible tener probabilidades negativas de transición entre estados."""

def markov_cadena_prob(P, v, n):
    """
    Calcula la distribución de probabilidad después de n pasos en una cadena de Markov en tiempo discreto.

    Args:
        P (numpy.ndarray): matriz de transición de la cadena de Markov.
        v (numpy.ndarray): vector inicial de distribución de probabilidad.
        n (int): número de pasos a calcular.

    Returns:
        numpy.ndarray: vector de distribución de probabilidad después de n pasos.
    """
    return np.dot(v, np.linalg.matrix_power(P, n))

#Calculamos distribucion desde despues de una hora(x1) hasta despues de 100 horas(x100) y visualizamos su evolucion
#Tomamos como vector inicial por ejemplo el de distribucion uniforme
p_state_t = [x00]
for i in range(1,100):
    p_state_t.append(markov_cadena_prob(P,x0,i))

print('\n----Distribucion desde despues de una hora(x1) hasta despues de 100 horas(x100)----\n')
state_distributions = pd.DataFrame(p_state_t)
print(state_distributions)

plt.plot(state_distributions)
plt.show()



