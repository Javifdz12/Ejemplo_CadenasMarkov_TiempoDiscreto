import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array(
    [[0.2, 0.5, 0.3],
    [0.4, 0.1, 0.5],
    [0.2, 0.5, 0.3]])

# Definir el vector inicial
x0 = np.array([0.7, 0.2, 0.1])

# Calcular la distribución después de una hora
print("\n----Distribución después de una hora----\n")
x1 = np.dot(x0,P)
print(x1)

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



