# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 9. Ejercicio 2

import numpy as np

# Algoritmo de Monte Carlo que verifica si B es la inversa de A
# basado en el metodo de Freivalds.
# Se generan vectores aleatorios x y se comprueba si A(Bx) = x y B(Ax) = x
# por propiedades de la matriz inversa, si se cumple esto
# B es la inversa de A.
# La funcion retorna True si B es la inversa de A, False en caso contrario.
def is_inverse(A, B, epsilon):
    n = A.shape[0]
    cantidad_iteraciones = int(np.log(1/epsilon))
    print("Iteraciones maximas a realizar segun epsilon: ", cantidad_iteraciones)

    # Tiempo de ejecucion: O(cantidad_iteraciones)
    for _ in range(cantidad_iteraciones):
        
        # Generar el vector aleatorio x
        x = np.random.rand(n, 1)  
        
        # Realiza la multiplicacion de matrices. 
        # Tiempo de ejecucion: O(n^2)
        y = A @ (B @ x)  
        z = B @ (A @ x)
        
        # Comprueba si la norma es mayor al epsilon buscado.
        # Si es mayor, significa que no es la inversa ya que los vectores obtenidos
        # se alejan del vector original x y por ende se retorna false
        if np.linalg.norm(y - x) > epsilon or np.linalg.norm(z - x) > epsilon:
            return False

    return True

# Matrices de prueba
A = np.array([[4, 7,9], [2, 6,1],[7,10,0]])
B = np.array([[3,-2,5],[9,0,-1],[4, 7,9]])
#B = np.linalg.inv(A)
epsilon = 0.000001
#epsilon = 0.000000000001


if is_inverse(A, B, epsilon):
    print("B es la inversa de A")
else:
    print("B no es la inversa de A")
