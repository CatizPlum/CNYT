"""
Librería de operaciones con números complejos.
Representación: cada número complejo es una tupla (real, imag).
"""
import math


# Suma
"""
Suma dos números complejos, representados como tuplas donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros:
    num1 (tupla): Primer número complejo, en formato (real, imag).
    num2 (tupla): Segundo número complejo, en formato (real, imag).

Retorna:
    tuple: Una tupla (real, imag) que representa la suma de los dos números complejos.
"""
def suma_complejos (num1, num2):
    real= num1[0] +  num2[0]
    imag= num1[1] + num2[1]
    return (real, imag)
# Producto
"""
Multiplica dos números complejos, representados como tuplas donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros:
    num1 (tupla): Primer número complejo, en formato (real, imag).
    num2 (tupla): Segundo número complejo, en formato (real, imag).

Retorna:
    tuple: Una tupla (real, imag) que representa la multiplicación de los dos números complejos.
"""
def producto_complejos (num1, num2):
    real= num1[0]*num2[0] + (-1)*(num1[1]*num2[1])
    imag= num1[0]*num2[1] + num1[1]*num2[0]
    return (real, imag)
# Resta
"""
Resta dos números complejos, representados como tuplas donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros:
    num1 (tupla): Primer número complejo, en formato (real, imag).
    num2 (tupla): Segundo número complejo, en formato (real, imag).

Retorna:
    tuple: Una tupla (real, imag) que representa la resta de los dos números complejos.
"""
def resta_complejos (num1, num2):
    real= num1[0] -  num2[0]
    imag= num1[1] - num2[1]
    return (real, imag)
# División
"""
Divide dos números complejos, representados como tuplas donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros
    num1 (tupla): Primer número complejo, en formato (real, imag).
    num2 (tupla): Segundo número complejo, en formato (real, imag).

Retorna:
    tuple: Una tupla (real, imag) que representa la división de los dos números complejos.
"""
def division_complejos (num1, num2):
    numerador_real= num1[0]*num2[0] + num1[1]*num2[1]
    numerador_imag= num1[0]*((-1)*num2[1]) + num1[1]*num2[0]
    denominador= num2[0]*num2[0] - ((-1)*num2[1]*num2[1])
    return (numerador_real/denominador, numerador_imag/denominador)
# Módulo
"""
Cálcula el módulo (magnitud) de un número complejo, representado como tupla donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros
    num (tupla): Número complejo, en formato (real, imag).

Retorna:
    float: El módulo del número complejo.
"""
def modulo_complejos (num):
    mod= (((num[0])**(2))+((num[1])**(2)))**(1/2)
    return (mod)
# Conjugado
"""
Cálcula el conjugado de un número complejo, representado como tupla donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros
    num (tupla): Número complejo, en formato (real, imag).

Retorna:
    tuple: El conjugado del número complejo.
"""
def conjugado_complejos (num):
    conjugado_real= num[0]
    conjugado_imag=((-1)*num[1])
    return (conjugado_real, conjugado_imag)

# Conversión entre representaciones polar y cartesiano, en los dos sentidos.
"""
Cálcula la conversión de un número complejo representado como tupla donde el primer componente es 
la parte real y el segundo la parte imaginaria a un número complejo representado como tupla donde
el primer componente es la magnitud (módulo) y el segundo la fase (ángulo). 

Parámetros
    num (tupla): Número complejo, en formato (real, imag).

Retorna:
    tuple: Número complejo, en formato (magnitud, fase).
"""
def cartes_polar (num):
    magnitud=modulo_complejos(num)
    angulo= math.atan(num[1]/num[0])
    return (magnitud, angulo)

"""
Cálcula la conversión de un número complejo representado como tupla donde el primer componente es 
la magnitud (módulo) y el segundo la fase (ángulo) a un número complejo representado como tupla donde
el primer componente es la parte real y el segundo la parte imaginaria.

Parámetros
    num (tupla): Número complejo, en formato (magnitud, fase).

Retorna:
    tuple: Número complejo, en formato (real, imag).
"""    
def polar_cartes (num):
    magnitud=num[0]
    angulo=num[1]
    x=magnitud*math.cos(angulo)
    y=magnitud* math.sin(angulo)
    return(x,y)

# Retornar la fase de un número complejo.
"""
Cálcula la fase (ángulo) de un número complejo, representado como tupla donde el primer componente es 
la parte real y el segundo la parte imaginaria. 

Parámetros
    num (tupla): Número complejo, en formato (real, imag).

Retorna:
    float: La fase del número complejo.
"""
def fase (num):
    fase= math.atan(num[1]/num[0])
    return(fase)