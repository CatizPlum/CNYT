# Ejercicios sobre Operaciones Matriciales y Vectoriales Complejas

#Este conjunto de ejercicios está diseñado para evaluar tu comprensión de diversos conceptos relacionados con las operaciones matriciales y vectoriales complejas, fundamentales en la computación cuántica. Cada ejercicio presenta un caso concreto para que apliques lo aprendido sobre productos internos complejos, matrices hermíticas, matrices unitarias y productos tensoriales.

#NOTA: VERIFICA TUS CÁLCULOS EN PAPEL Y EN LA COMPUTADORA.

## Ejercicio 1: Producto interno complejo para vectores columna

#Dados dos vectores columna complejos:

#$$ \mathbf{a} = \begin{bmatrix} 1 + 2i \\ 3 - 4i \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 2 - i \\ -1 + 3i \end{bmatrix} $$

#Calcula el producto interno complejo $ \langle \mathbf{a}, \mathbf{b} \rangle $.

import numpy as np

a = np.array([[1 + 2j], [3 - 4j]])
b = np.array([[2 - 1j], [-1 + 3j]])

inner_product = np.vdot(a, b) 

print(f"a = \n{a}")
print(f"b = \n{b}")
print(f"Producto interno <a, b> = {inner_product}")

## Ejercicio 2: Producto interno complejo para matrices complejas cuadradas

#Dadas dos matrices complejas cuadradas:

#$$ A = \begin{bmatrix} 1+i y 2-2i \\ 3+3i y 4-i \end{bmatrix}, \quad B = \begin{bmatrix} 1-2i y 3+i \\ 4-4i y 2+2i \end{bmatrix} $$

#Calcula el producto interno complejo $ \langle A, B \rangle $.

import numpy as np

# Definir dos matrices cuadradas complejas
matriz_A = np.array([[1+1j, 2-2j],
                     [3+3j, 4-1j]])

matriz_B = np.array([[1-2j, 3+1j],
                     [4-4j, 2+2j]])

producto_interno_matriz = np.trace(np.dot(np.conjugate(matriz_A).T, matriz_B))
print("\nProducto interno complejo ⟨A, B⟩ =", producto_interno_matriz)



# Ejercicios sobre autovalores y autovectores

## Ejercicio 1: Calcular autovalores y autovectores de una matriz real

#Calcula los autovalores y autovectores de la siguiente matriz real:

#$$
#A = \begin{pmatrix}
#4 & 1 \\
#2 & 3
#\end{pmatrix}
#$$
import numpy as np

A = np.array([[4, 1], [2, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
#**Pista:** Usa `numpy.linalg.eig`.

## Ejercicio 2: Autovalores y autovectores de una matriz compleja

#Calcula los autovalores y autovectores de la siguiente matriz compleja:

#$$
#B = \begin{pmatrix}
#1 + 2i & 2 + 3i \\
#4 + 5i & 6 + 7i
#\end{pmatrix}
#$$

#donde \(i\) es la unidad imaginaria.
B = np.array([[1+2j, 2+3j],
              [4+5j, 6+7j]], dtype=complex)

eigenvals_B, eigenvecs_B = np.linalg.eig(B)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
#**Sugerencia:** Asegúrate de que tu matriz esté definida con números complejos en Python usando `dtype=complex`.

## Ejercicio 3: Descomposición propia de matrices simétricas

#Calcula los autovalores y autovectores de la siguiente matriz simétrica:

#$$
#C = \begin{pmatrix}
#5 & 4 \\
#4 & 5
#\end{pmatrix}
#$$
import numpy as np
C = np.array([[5, 4],
              [4, 5]])

eigenvalues, eigenvectors = np.linalg.eig(C)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
#Analiza las propiedades de los autovectores y autovalores de matrices simétricas basándote en tus resultados.

#La matriz utilizada es simétrica, y eso hace que sus autovalores siempre sean números reales, como los obenidos: 9 y 1. 
# #Los autovectores que aparecen junto a ellos son perpendiculares entre sí y tienen longitud uno, lo que significa que 
# #forman una base ortonormal.

print("\nProducto punto de autovectores:", np.dot(eigenvectors[:, 0], eigenvectors[:, 1]))
print("¿Son ortogonales?", np.isclose(np.dot(eigenvectors[:, 0], eigenvectors[:, 1]), 0))


## Ejercicio 4: Trazado de transformaciones de matrices

#Considera la matriz:

#$$
#T = \begin{pmatrix}
#2 & 1 \\
#1 & 3
#\end{pmatrix}
#$$

#1. Traza la circunferencia unitaria.
#2. Aplica la matriz \(T\) para transformar la circunferencia unitaria.
#3. Traza la figura transformada.
#4. Demuestre gráficamente que los vectores propios solo se multiplican por un escalar al transformarse. (Dibuje los vectores propios y los transformados).

#Explique cómo la matriz \(T\) transforma la circunferencia unitaria según el gráfico resultante.
import numpy as np
import matplotlib.pyplot as plt
T = np.array([[2, 1],
              [1, 3]])

# Calcular autovalores y autovectores de T
eigvals_T, eigvecs_T = np.linalg.eig(T)
print(f"Autovalores de T: {eigvals_T}")
print(f"Autovectores de T:\n{eigvecs_T}")

# Crear la figura
plt.figure(figsize=(8, 8))

# 1. Generar circunferencia unitaria
theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])

# 2. Aplicar transformación
transformed_circle = T @ circle

# 3. Graficar circunferencias
plt.plot(circle[0], circle[1], 'b-', linewidth=2, label='Circunferencia unitaria')
plt.plot(transformed_circle[0], transformed_circle[1], 'r-', linewidth=2, label='Transformada por T')

# 4. Graficar autovectores (normalizados) y sus transformados
# Normalizar autovectores para que tengan longitud 1
v1 = eigvecs_T[:, 0] / np.linalg.norm(eigvecs_T[:, 0])
v2 = eigvecs_T[:, 1] / np.linalg.norm(eigvecs_T[:, 1])

# Graficar autovectores normalizados
plt.quiver(0, 0, v1[0], v1[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='green', width=0.03,
           label=f'Autovector 1 (normalizado)')
plt.quiver(0, 0, v2[0], v2[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='orange', width=0.03,
           label=f'Autovector 2 (normalizado)')

# Graficar autovectores transformados
transformed_v1 = T @ v1
transformed_v2 = T @ v2

plt.quiver(0, 0, transformed_v1[0], transformed_v1[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='green', width=0.01, alpha=0.7,
           label=f'T·v1 (escalado por λ={eigvals_T[0]:.2f})')
plt.quiver(0, 0, transformed_v2[0], transformed_v2[1], 
           angles='xy', scale_units='xy', scale=1, 
           color='orange', width=0.01, alpha=0.7,
           label=f'T·v2 (escalado por λ={eigvals_T[1]:.2f})')

# Configurar el gráfico
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.legend(loc='upper right', fontsize=9)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.tight_layout()
plt.show()


#**Pista:** Use `numpy` para operaciones con matrices y `matplotlib` para graficar.
#Es evidente que el circulo unitario se transforma en una aelipse y que al multiplicar
# los vectores no cambia su dirección sino únicamente su longitud.

## Ejercicio 5: Descomposición propia de matrices diagonales

#Calcule los valores propios y los vectores propios de la siguiente matriz diagonal:

#$$
#D = \begin{pmatrix}
#7 & 0 \\
#0 & -3
#\end{pmatrix}
#$$
import numpy as np
D = np.array([[7, 0],
              [0, -3]])

eigenvals_D, eigenvecs_D = np.linalg.eig(D)

print("Eigenvalues:", eigenvals_D)
print("Eigenvectors:\n", eigenvecs_D)

#Discuta la importancia de los valores propios y los vectores propios para matrices diagonales.

#Es evidente que los vectores propios de una matriz diagonal forman una base canónica, y los valores porpios
#son aquellos que están en la diagonal.