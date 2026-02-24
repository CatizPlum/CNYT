
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as iw

## Ejercicio 1: Operaciones básicas con números complejos
#1. Calcula manualmente y luego verifica con Python el resultado de `(3 + 4j) + (1 - 2j)`, `(5 + 6j) * (7 - 8j)` y `(2 - 3j) / (1 + 4j)`.

z1=complex(3,4)
z2=complex(1,-2)
z3=complex(5,6)
z4=complex(7,-8)
z5=complex(2,-3)
z6=complex(1,4)

print("Suma:", z1 + z2) #(3 + 4j) + (1 - 2j) = (4,2i)
print("Multiplicacion:", z3 * z4) #(5 + 6j) * (7 - 8j) = (83,2j)
print("Division:", z5 / z6) #(2 - 3j) / (1 + 4j) = (-10,-11j)/17

#2. Encuentra el conjugado y el módulo de `(3 - 4j)`.
z7=complex(3,-4)

print("Conjugado de z7:", z7.conjugate()) #(3 - 4j)= 3+4j


## Ejercicio 2: Visualización de operaciones complejas
#1. Escribe una función de Python para representar gráficamente un número complejo en el plano complejo. Úsala para representar gráficamente `(3 + 4j)` y su conjugado.

import matplotlib.pyplot as plt

def graficar_complejos(z1, z2):
    # Graficar el primer número complejo
    plt.scatter(z1.real, z1.imag, color='blue', label=f'{z1}')
    # Graficar el segundo número complejo (por ejemplo, el conjugado)
    plt.scatter(z2.real, z2.imag, color='red', label=f'{z2}')
    
    # Dibujar ejes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Configuración del gráfico
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.legend()
    plt.grid(True)
    plt.title('Plano Complejo')
    plt.show()

z = 3 + 4j
z_conj = z.conjugate()

graficar_complejos(z, z_conj)

#2. Extiende la función para mostrar gráficamente la suma y la multiplicación de dos números complejos.

def graficar_operaciones(z1, z2):
    # Calcular suma y producto
    suma = z1 + z2
    producto = z1 * z2
    
    # Graficar los números originales
    plt.scatter(z1.real, z1.imag, color='blue', label=f'{z1}')
    plt.scatter(z2.real, z2.imag, color='red', label=f'{z2}')
    
    # Graficar la suma
    plt.scatter(suma.real, suma.imag, color='green', label=f'Suma: {suma}')
    
    # Graficar el producto
    plt.scatter(producto.real, producto.imag, color='purple', label=f'Producto: {producto}')
    
    # Dibujar ejes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Configuración del gráfico
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.legend()
    plt.grid(True)
    plt.title('Operaciones con Números Complejos')
    plt.show()

z8 = 3 + 4j
z9 = 5 - 7j

graficar_operaciones(z8, z9)


## Ejercicio 3: Exploración del conjunto de Mandelbrot
#1. Modifica el código del conjunto de Mandelbrot proporcionado para cambiar su nivel de zoom y su punto central. Observa cómo cambia el patrón fractal.
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

pixels = 800

# --- Primer fractal (vista general) ---
max_iter1 = 30
x1 = np.linspace(-2, 1, pixels)
y1 = np.linspace(-1.5, 1.5, pixels)
xx1, yy1 = np.meshgrid(x1, y1)
c1 = xx1 + yy1*1j
mandelbrot_set1 = np.array([mandelbrot(ci, max_iter1) for ci in c1.ravel()]).reshape(c1.shape)

# --- Segundo fractal (zoom) ---
max_iter2 = 50
x2 = np.linspace(-0.9, -0.6, pixels)
y2 = np.linspace(-0.2, 0.2, pixels)
xx2, yy2 = np.meshgrid(x2, y2)
c2 = xx2 + yy2*1j
mandelbrot_set2 = np.array([mandelbrot(ci, max_iter2) for ci in c2.ravel()]).reshape(c2.shape)

# --- Mostrar ambas gráficas juntas ---
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico 1
im1 = axes[0].imshow(mandelbrot_set1, extent=[x1.min(), x1.max(), y1.min(), y1.max()])
axes[0].set_title("Mandelbrot Set (Vista general)")
fig.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)

# Gráfico 2
im2 = axes[1].imshow(mandelbrot_set2, extent=[x2.min(), x2.max(), y2.min(), y2.max()])
axes[1].set_title("Mandelbrot Set (Zoom)")
fig.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()
# Es evidente que a medida que los valores se hacen más pequeños se desdibuja la figura inicial del conjunto de mandelbrot y nos acercamos cada 
#vez más a la parte amarilla de la gráfica, es importante aclarar que se muestran ambas gráficas juntas con el propósito de comparar más facilmente 
#pero inicialmente se ejecutaron cada una por separado.

#2. Experimenta con diferentes valores de `max_iter` y observa el efecto en el detalle del fractal y el tiempo de cálculo.

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

pixels = 800

# --- Primer cálculo con max_iter=30 ---
max_iter1 = 30
x = np.linspace(-2, 1, pixels)
y = np.linspace(-1.5, 1.5, pixels)
xx, yy = np.meshgrid(x, y)
c = xx + yy*1j
mandelbrot_set1 = np.array([mandelbrot(ci, max_iter1) for ci in c.ravel()]).reshape(c.shape)

# --- Segundo cálculo con max_iter=300 ---
max_iter2 = 300
mandelbrot_set2 = np.array([mandelbrot(ci, max_iter2) for ci in c.ravel()]).reshape(c.shape)

# --- Mostrar ambas gráficas juntas ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1
im1 = axes[0].imshow(mandelbrot_set1, extent=[-2, 1, -1.5, 1.5])
axes[0].set_title(f"Mandelbrot Set (max_iter={max_iter1})")
fig.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)

# Gráfico 2
im2 = axes[1].imshow(mandelbrot_set2, extent=[-2, 1, -1.5, 1.5])
axes[1].set_title(f"Mandelbrot Set (max_iter={max_iter2})")
fig.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)

plt.subplots_adjust(wspace=0.4)  
plt.show()
# Es evidente que a medida que aumenta el número de iteraciones el tiempo de ejecucion aumenta, 
#es importante aclarar que se muestran ambas gráficas juntas con el propósito de comparar más facilmente 
#pero inicialmente se ejecutaron cada una por separado.

## Ejercicio 4: Creación de un conjunto de Julia
#1. Implementa un generador de conjuntos de Julia. Usa una constante como `-0.4 + 0.6j` para la iteración `z = z*z + constante`.
import numpy as np
import matplotlib.pyplot as plt

def julia_set(c, xlim, ylim, pixel_density, max_iter):
    """
    Genera el conjunto de Julia para una constante c dada.
    
    Parámetros:
    - c: constante compleja
    - xlim, ylim: límites del plano complejo (xmin, xmax), (ymin, ymax)
    - pixel_density: número de puntos por unidad
    - max_iter: número máximo de iteraciones
    """
    x = np.linspace(xlim[0], xlim[1], int((xlim[1] - xlim[0]) * pixel_density))
    y = np.linspace(ylim[0], ylim[1], int((ylim[1] - ylim[0]) * pixel_density))
    
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    julia = np.zeros(Z.shape, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(Z) < 2
        julia[mask] += 1
        Z[mask] = Z[mask] ** 2 + c
    
    return X, Y, julia

# Parámetros
c = complex(-0.4, 0.6)
xlim = (-1.5, 1.5)
ylim = (-1.5, 1.5)
pixel_density = 300
max_iter = 50

# Generar conjunto de Julia
X, Y, julia = julia_set(c, xlim, ylim, pixel_density, max_iter)

# Visualización
plt.figure(figsize=(8, 8))
plt.imshow(julia, extent=[xlim[0], xlim[1], ylim[0], ylim[1]], cmap='inferno', origin='lower')
plt.colorbar(label='Iteraciones')
plt.title(f'Conjunto de Julia para c = {c}')
plt.xlabel('Parte real')
plt.ylabel('Parte imaginaria')
plt.show()
#2. Explora cómo al cambiar la constante se modifica el patrón del conjunto de Julia.
# Definir una lista de constantes para explorar
constants = [
    complex(-0.4, 0.6),
    complex(-0.8, 0.156),
    complex(-0.7269, 0.1889)
]

# Parámetros comunes
xlim = (-1.5, 1.5)
ylim = (-1.5, 1.5)
pixel_density = 300
max_iter = 50

# Generar y mostrar los conjuntos de Julia
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, c in zip(axes, constants):
    X, Y, julia = julia_set(c, xlim, ylim, pixel_density, max_iter)
    im = ax.imshow(julia, extent=[xlim[0], xlim[1], ylim[0], ylim[1]], cmap='inferno', origin='lower')
    ax.set_title(f'c = {c}')
    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    plt.colorbar(im, ax=ax)

plt.tight_layout()
plt.show()
#Es evidente que a pequeños cambios en las constantes, la imagen del conjunto julia puede sufiri grandes deformaciones.
#Fuente: https://mathworld.wolfram.com/JuliaSet.html

## Ejercicio 5: Propiedades de los números complejos
#1. Demuestra que el valor absoluto del producto de dos números complejos es el producto de sus valores absolutos.

# Definimos las variables reales
a, b, c, d = 1, 2, 3, 1   

# Definimos los números complejos
z1 = complex(a, b)   # a + bi
z2 = complex(c, d)   # c + di

# Producto
producto = z1 * z2

print("=== Demostración |z1 * z2| = |z1| * |z2| ===")
print(f"z1 = {a} + {b}i")
print(f"z2 = {c} + {d}i")
print(f"z1 * z2 = ({a} + {b}i)({c} + {d}i) = ({a*c - b*d}) + ({a*d + b*c})i")

# Valor absoluto del producto
lhs = abs(producto)
print("\n|z1 * z2| = sqrt((Re)^2 + (Im)^2)")
print(f"= sqrt(({a*c - b*d})^2 + ({a*d + b*c})^2)")
print(f"= {lhs}")

# Producto de los valores absolutos
abs_z1 = abs(z1)
abs_z2 = abs(z2)
rhs = abs_z1 * abs_z2
print("\n|z1| = sqrt(a^2 + b^2) = sqrt({a}^2 + {b}^2) = {abs_z1}")
print("|z2| = sqrt(c^2 + d^2) = sqrt({c}^2 + {d}^2) = {abs_z2}")
print(f"|z1| * |z2| = {abs_z1} * {abs_z2} = {rhs}")

print("\nConclusión: |z1 * z2| =", lhs, "=", rhs)

#2. Demuestra que el conjugado de la suma de dos números complejos es la suma de sus conjugados.

# Definimos las variables reales
a, b, c, d = 1, 2, 3, 1   

# Definimos los números complejos
z1 = complex(a, b)   # a + bi
z2 = complex(c, d)   # c + di

print("\n=== Demostración conjugado(z1 + z2) = conjugado(z1) + conjugado(z2) ===")
print(f"z1 = {a} + {b}i")
print(f"z2 = {c} + {d}i")

# Conjugado de la suma
suma = z1 + z2
lhs = suma.conjugate()
print(f"z1 + z2 = ({a} + {b}i) + ({c} + {d}i) = ({a+c}) + ({b+d})i")
print(f"conjugado(z1 + z2) = ({a+c}) - ({b+d})i = {lhs}")

# Suma de los conjugados
rhs = z1.conjugate() + z2.conjugate()
print(f"conjugado(z1) = {a} - {b}i")
print(f"conjugado(z2) = {c} - {d}i")
print(f"conjugado(z1) + conjugado(z2) = ({a} - {b}i) + ({c} - {d}i) = ({a+c}) - ({b+d})i = {rhs}")

print("\nConclusión: conjugado(z1 + z2) =", lhs, "=", rhs)
