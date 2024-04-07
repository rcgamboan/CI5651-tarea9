# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 9. Ejercicio 3

import random

# Algoritmo probabilistico para encontrar una aproximacion 
# del conjunto de vertices de una cubierta de vertices de un grafo
# La principal diferencia del algoritmo deterministico es que
# en lugar de seleccionar siempre el vertice con mayor grado,
# para lo cual se deben recorrer todos los vertices del grafo,
# selecciona aleatoriamente una arista y agrega ambos vertices
# al conjunto de vertices cubiertos. Luego, elimina todas las aristas
# Retorna el conjunto de vertices cubiertos.
def approx_vertex_cover_probabilistic(G): 
    
    # Inicializa el conjunto de vertices y aristas
    V = set()
    E = set(G.edges())
    # Se ejecuta hasta que todas las aristas esten cubiertas
    # Tiempo: O(n), con n el numero de aristas
    while E:  
        
        # Selecciona una arista aleatoria. Tiempo: O(1)
        u, v = random.choice(list(E))

        V.add(u)
        V.add(v)
        
        # Elimina las aristas que estan conectadas a los vertices seleccionados
        E -= set(G.edges([u, v]))  

    return V
