# Ejercicios sobre Operaciones Matriciales y Vectoriales Complejas

#Este conjunto de ejercicios está diseñado para evaluar tu comprensión de diversos conceptos relacionados con las operaciones matriciales y vectoriales complejas, fundamentales en la computación cuántica. Cada ejercicio presenta un caso concreto para que apliques lo aprendido sobre matrices hermíticas, matrices unitarias y productos tensoriales.

#NOTA: VERIFICA TUS CÁLCULOS EN PAPEL Y EN LA COMPUTADORA.

## Ejercicio 1: Matrices Hermíticas Complejas

#Considera la matriz:

#$$ H = \begin{bmatrix} 3 & 2+i \\ 2-i & 1 \end{bmatrix} $$

#- Verifica si $H$ es una matriz hermítica.
#- Si lo es, encuentra sus valores propios.
import numpy as np

H = np.array([[3, 2+1j], [2-1j, 1]])
is_hermitian = np.allclose(H, H.conj().T)
eigenvalues = np.linalg.eigvalsh(H)  

print("¿Es Hermitiana?", is_hermitian)
print("Valores propios:", eigenvalues)
## Ejercicio 2: Matrices unitarias complejas

#Considere la matriz:

#$$ U = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & i \\ i & 1 \end{bmatrix} $$

#- Verifique si $ U $ es una matriz unitaria.
#- Calcule $ UU^\dagger $ para confirmar su unitaridad, donde $ U^\dagger $ denota la transpuesta conjugada de $ U $.

import numpy as np

# Define la matriz unitaria compleja
unitary_matrix = (1/np.sqrt(2)) * np.array([[1, 1j], [1j, 1]])

# Verifica si la matriz es unitaria
# np.eye(2) devuelve la identidad de tamaño 2x2
is_unitary = np.allclose(np.dot(unitary_matrix, unitary_matrix.conj().T), np.eye(2))

print("¿Es unitaria?", is_unitary)
print("Matriz unitaria:\n", unitary_matrix)

import numpy as np

# Define la matriz unitaria compleja
U = (1/np.sqrt(2)) * np.array([[1, 1j], [1j, 1]])

# Calcula la conjugada transpuesta (dagger)
U_dagger = U.conj().T

# Calcula U * U^\dagger
UU_dagger = np.dot(U, U_dagger)

# Verifica si es unitaria (debe ser igual a la identidad)
is_unitary = np.allclose(UU_dagger, np.eye(2))

print("\nProducto U * U^+:")
print(UU_dagger)
print("\n¿Es unitaria?", is_unitary)

#Ejercicio 3: Producto tensorial para vectores complejos

#Dados los vectores complejos:

#$$ \mathbf{v} = \begin{bmatrix} 1+i \\ 2-i \end{bmatrix}, \quad \mathbf{w} = \begin{bmatrix} 1-2i \\ 3 \end{bmatrix} $$

#Calcula el producto tensorial $ \mathbf{v} \otimes \mathbf{w} $.

v = np.array([1+1j, 2-1j])
w = np.array([1-2j, 3])
tensor = np.kron(v, w)
print(tensor)

## Ejercicio 4: Producto tensorial para matrices complejas

#Dadas las matrices:

#$$ M_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad M_2 = \begin{bmatrix} i & 0 \\ 0 & -i \end{bmatrix} $$

#Calcula el producto tensorial $ M_1 \otimes M_2 $.

M1 = np.array([[0, 1], [1, 0]])
M2 = np.array([[1j, 0], [0, -1j]])
tensor = np.kron(M1, M2)
print(tensor)

## Ejercicio 5: Modelado de cálculos cuánticos con vectores y matrices

#Utilizando matrices y vectores, implementa un modelo del interferómetro de Mach/Zehnder.
import numpy as np

# Definir matrices
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
X = np.array([[0, 1], [1, 0]])

# Estado inicial |0>
estado_inicial = np.array([1, 0])

# Aplicar H 
estado = np.dot(H, estado_inicial)
print("Después de H:", estado)

# Aplicar X 
estado = np.dot(X, estado)
print("Después de X:", estado)

# Aplicar H 
estado_final = np.dot(H, estado)
print("Estado final:", estado_final)

# Verificar probabilidades
prob_0 = np.abs(estado_final[0])**2
prob_1 = np.abs(estado_final[1])**2
print("\nProbabilidad de medir |0>:", prob_0)
print("Probabilidad de medir |1>:", prob_1)

## Ejercicio 6: Composición de sistemas cuánticos

#Utilizando matrices y vectores, implementa un modelo del siguiente circuito.

#Utilice la siguiente matriz para $U_f$:

import numpy as np

# Definir compuerta Hadamard
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])

# Definir U_f (matriz 4x4 dada)
U_f = np.array([[0, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

print("=== CANAL |0> ===")
print("Evolución: |0> → H → U_f → H")

# Estado inicial |0> 
estado_inicial_0 = np.array([1, 0])  # |0>

# Aplicar H 
estado_H = np.dot(H, estado_inicial_0)
print("\nDespués de H:", estado_H)

# tensor
estado_2qubits = np.kron(estado_H, np.array([1, 0]))  
print(estado_2qubits)

# Aplicar U_f
estado_Uf = np.dot(U_f, estado_2qubits)
print(estado_Uf)


primer_qubit = estado_Uf[0:2]  
estado_final_0 = np.dot(H, primer_qubit)
print("Después de H final:", estado_final_0)


print("=== CANAL |1> ===")
print("Evolución: |1> → H → U_f")

# Estado inicial |1>
estado_inicial_1 = np.array([0, 1])  # |1>

# Aplicar H 
estado_H_1 = np.dot(H, estado_inicial_1)
print("\nDespués de H:", estado_H_1)
# tensor
estado_2qubits_1 = np.kron(estado_H_1, np.array([1, 0]))  # |ψ> ⊗ |0>
print("Expandido a 2 qubits (⊗|0>):", estado_2qubits_1)

# Aplicar U_f 
estado_final_1 = np.dot(U_f, estado_2qubits_1)
print("Después de U_f (estado final):", estado_final_1)

