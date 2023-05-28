import networkx as nx
import matplotlib.pyplot as plt
from math import pi,atan2,degrees
# Definimos los estados
states = ['A', 'B', 'C']

# Definimos la matriz de transición
transitions = [
    [0.2, 0.5, 0.3],
    [0.4, 0.1, 0.5],
    [0.2, 0.5, 0.3]
]

# Creamos el grafo
G = nx.DiGraph()

# Añadimos los estados
G.add_nodes_from(states)

# Añadimos las transiciones
for i in range(len(states)):
    for j in range(len(states)):
        if transitions[i][j] != 0:
            G.add_edge(states[i], states[j], weight=transitions[i][j])


# Dibujamos el grafo
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_labels(G, pos)

# Agregamos los pesos de las aristas
for u, v, data in G.edges(data=True):

    weight = data['weight']
    x, y = pos[u]
    dx, dy = pos[v][0] - pos[u][0], pos[v][1] - pos[u][1]
    angle = atan2(dy, dx)
    angle = angle + pi if pi / 2 < angle < 3 * pi / 2 else angle

    if u == v:
        offset_x = 0.08
        offset_y = 0.1
        pos_text = (x + offset_x, y + offset_y)
    else:
        pos_text = (x + 0.2 * dx, y + 0.2 * dy)

    plt.text(*pos_text, f"{weight:.2f}", ha='center', va='center', rotation=degrees(angle), fontsize=10, color='red')


plt.axis('off')
plt.show()





