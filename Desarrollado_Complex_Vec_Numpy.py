# Ejercicios sobre Vectores y Matrices Complejos con Casos Concretos

#Este conjunto de ejercicios se centra en operaciones con vectores columna complejos y matrices cuadradas complejas, incluyendo casos concretos con vectores y matrices escritos en formato LaTeX.
import numpy as np
## Operaciones con Vectores Columna Complejos

### Ejercicio 1: Suma de Dos Vectores Complejos
#Dados dos vectores complejos
#$ v1 = \begin{bmatrix} 1 + 2i \\ 3 - i \end{bmatrix} $
#y
#$ v2 = \begin{bmatrix} 2 - i \\ 4 + 2i \end{bmatrix} $,
#halla su suma.

v1 = np.array([1 + 2j, 3 - 1j])
v2 = np.array([2 - 1j, 4 + 2j])

print("=== Entrada ===")
print("v1 =", v1)
print("v2 =", v2)

suma = v1 + v2
print("\n=== Resultado ===")
print("v1 + v2 =", suma)

### Ejercicio 2: Negación de un Vector Complejo
#Dado un vector complejo
#$ v = \begin{bmatrix} 2 + 3i \\ 1 - 2i \end{bmatrix} $,
#halla su negación.

v1 = np.array([2 + 3j, 1 - 2j])

print("=== Entrada ===")
print("v1 =", v1)

neg = -v1
print("\n=== Resultado ===")
print("-v1", neg)

### Ejercicio 3: Multiplicación de un vector complejo por un escalar
#Multiplica el vector complejo
#$ v = \begin{bmatrix} 1 - i \\ 2 + 2i \end{bmatrix} $
#por el escalar complejo $$ 3 + i $$.

v = np.array([1 - 1j, 2 + 2j]) 
esc = 3 + 1j 

print("=== Entrada ===") 
print("v =", v) 
print("esc =", esc) 

res = esc * v 
print("\n=== Resultado ===") 
print("esc * v =", res)

### Ejercicio 4: Transpuesta de un vector complejo
#Encuentra la transpuesta del vector complejo
#$ v = \begin{bmatrix} 2 - i \\ 3 + 4i \end{bmatrix} $.

v = np.array([[2 - 1j], [3 + 4j]]) 

print("\n=== Entrada ===") 
print("v =\n", v) 

res = v.T 
print("\n=== Resultado ===") 
print("v.T =", res)

### Ejercicio 5: Conjugado de un vector complejo
#Calcula el conjugado del vector complejo
#$ v = \begin{bmatrix} 1 + i \\ 2 - 3i \end{bmatrix} $.

v = np.array([1 + 1j, 2 - 3j]) 

print("\n=== Entrada ===") 
print("v =", v) 

res = np.conjugate(v) 
print("\n=== Resultado ===") 
print("conjugado(v) =", res)

### Ejercicio 6: Adjunto (Transpuesta Conjugada) de un Vector Complejo
#Encuentra el adjunto (o transpuesta conjugada) del vector complejo
#$ v = \begin{bmatrix} 1 - 2i \\ 3 + i \end{bmatrix} $.

v = np.array([[1 - 2j], [3 + 1j]]) 

print("\n=== Entrada ===") 
print("v =\n", v) 

res = v.T.conj()
print("\n=== Resultado ===") 
print("adjunto(v) =", res)

## Operaciones con Matrices Cuadradas Complejas

### Ejercicio 7: Suma de Dos Matrices Complejas
#Dadas dos matrices complejas
#$ m1 = \begin{bmatrix} 1 + i & 2 - i \\ 3 + 2i & 4 \end{bmatrix} $
#y
#$ m2 = \begin{bmatrix} 2 - 3i & 1 \\ i & 2 + 2i \end{bmatrix} $,
#calcula su suma.

m1 = np.array([[1 + 1j, 2 - 1j], [3 + 2j, 4]]) 
m2 = np.array([[2 - 3j, 1], [1j, 2 + 2j]]) 

print("\n=== Entrada ===") 
print("m1 =\n", m1) 
print("m2 =\n", m2) 

res = m1 + m2 
print("\n=== Resultado ===") 
print("m1 + m2 =\n", res)

### Ejercicio 8: Negación de una matriz compleja
#Calcula la negación de la matriz compleja
#$ m = \begin{bmatrix} 2 + i & 3 \\ 1 - i & 2 + 2i \end{bmatrix} $.

m = np.array([[2 + 1j, 3], [1 - 1j, 2 + 2j]]) 

print("\n=== Entrada ===") 
print("m =\n", m) 

res = -m 
print("\n=== Resultado ===") 
print("-m =\n", res)

### Ejercicio 9: Multiplicación de una matriz compleja por un escalar
#Multiplica la matriz compleja
#$ m = \begin{bmatrix} 1 - i & 2 \\ 3 + i & 4 - 2i \end{bmatrix} $
#por el escalar complejo $$ 2 + 3i $$.

m = np.array([[1 - 1j, 2], [3 + 1j, 4 - 2j]]) 
esc = 2 + 3j 

print("\n=== Entrada ===") 
print("m =\n", m) 
print("esc =", esc) 

res = m * esc 
print("\n=== Resultado ===") 
print("esc * m =\n", res)

### Ejercicio 10: Conjugado de una matriz compleja
#Calcula el conjugado de la matriz compleja
#$ m = \begin{bmatrix} 1 + i & 2 \\ 3 - i & 4 + 2i \end{bmatrix} $.

m = np.array([[1 + 1j, 2], [3 - 1j, 4 + 2j]]) 

print("\n=== Entrada ===") 
print("m =\n", m)

res = np.conjugate(m) 
print("\n=== Resultado ===") 
print("conjugado(m) =\n", res)

### Ejercicio 11: Transpuesta de una matriz compleja
#Calcula la transpuesta de la matriz compleja
#$ m = \begin{bmatrix} 1 - i & 2 + 2i \\ 3 & 4 - i \end{bmatrix} $.

m = np.array([[1 - 1j, 2 + 2j], [3, 4 - 1j]]) 

print("\n=== Entrada ===") 
print("m =\n", m) 

res = m.T 
print("\n=== Resultado ===") 
print("m.T =\n", res)

### Ejercicio 12: Adjunto (Transpuesta conjugada) de una matriz compleja
#Calcula el adjunto (o transpuesta conjugada) de la matriz compleja
#$ m = \begin{bmatrix} 1 + 2i & 3 - i \\ 4 & 5 + i \end{bmatrix} $.

m = np.array([[1 + 2j, 3 - 1j], [4, 5 + 1j]]) 

print("\n=== Entrada ===") 
print("m =\n", m) 

res = m.T.conj() 
print("\n=== Resultado ===") 
print("adjunto(m) =\n", res)

### Ejercicio 13: Comprobación de las dimensiones de una matriz
#Determina las dimensiones de la matriz compleja
#$ m = \begin{bmatrix} 1 - i & 2 \\ 3 + 2i & 4 - i \end{bmatrix} $.

m = np.array([[1 - 1j, 2], [3 + 2j, 4 - 1j]]) 

print("\n=== Entrada ===") 
print("m =\n", m) 

print("\n=== Resultado ===") 
print("dimensiones =", m.shape)

## Multiplicación de Matrices y Vectores

### Ejercicio 14: Multiplicación de una Matriz Cuadrada Compleja por un Vector Columna Complejo
#Multiplica la matriz cuadrada compleja
#$ m = \begin{bmatrix} 1 + i & 2 - i \\ 3 & 4 + i \end{bmatrix} $
#por el vector columna complejo
#$ v = \begin{bmatrix} 2 - i \\ 1 + 3i \end{bmatrix} $.

m = np.array([[1 + 1j, 2 - 1j], [3, 4 + 1j]]) 
v = np.array([[2 - 1j], [1 + 3j]]) 

print("\n=== Entrada ===") 
print("m =\n", m) 
print("v =\n", v) 

res = np.dot(m, v) 
print("\n=== Resultado ===") 
print("m * v =\n", res)

## Instrucciones
#En cada ejercicio, asegúrese de mostrar tanto la entrada (vectores/matrices) como el resultado de la operación. Use NumPy para estos ejercicios y practique el manejo de números complejos y operaciones con matrices en Python.

