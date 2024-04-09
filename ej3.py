# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 9. Ejercicio 3

import random
import networkx as nx

# Algoritmo probabilistico para encontrar una aproximacion 
# del conjunto de vertices de una cubierta de vertices de un grafo
# La principal diferencia del algoritmo deterministico es que
# en lugar de seleccionar siempre el vertice con mayor grado,
# para lo cual se deben recorrer todos los vertices del grafo,
# selecciona aleatoriamente una arista y agrega ambos vertices
# al conjunto de vertices cubiertos. Luego, elimina todas las aristas
# Retorna el conjunto de vertices cubiertos.
def min_vertex_cover(G): 
    
    # Inicializa el conjunto de vertices y aristas
    V = set()
    E = set(G.edges())
    # Se ejecuta hasta que todas las aristas esten cubiertas
    # Tiempo: O(n), con n el numero de aristas
    while E:  
        
        # Selecciona una arista aleatoria. Tiempo: O(1)
        u,v = random.choice(list(E))
        V.add(u)
        V.add(v)
        
        # Elimina las aristas que estan conectadas a los vertices seleccionados
        E -= set(G.edges([u, v]))  

    return V

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
G.add_edges_from([(1, 4), (5, 7), (7, 8),(3,1),(4,2)])

vertex_cover = min_vertex_cover(G)

print("Aristas del minimo cubrimiento:", vertex_cover)