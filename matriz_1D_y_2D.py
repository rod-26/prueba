import numpy as np 

# Matriz 1D
a=np.array([1,2,3])
print("1D array: ")
print(a)
print()

# Matriz 1D
b=np.array([(1,2,3),(4,5,6)])
print("2D array: ")
print(b)
print()

# matriz de numeros 1 de tres filas y 4 columnas
unos=np.ones((3,4))
print(unos)
print()

# matriz de numeros 0 de tres filas y 4 columnas
ceros=np.zeros((3,4))
print(ceros)
print()

# matriz de numeros aleatorios de tres filas y 4 columnas
aleatorios=np.random.random((3,4))
print(aleatorios)
print()

# matriz vacias de tres filas y 4 columnas
vacia=np.empty((3,4))
print(vacia)
print()

# matriz de un solo valor de tres filas y 4 columnas
full=np.full((3,4),8)
print(full)
print()

# matriz con valores espaciados uniformemente que empieza de 0 hasta el 30 de 5 en 5
espacio1=np.arange(0,30,5)
print(espacio1)
print()

# matriz con valores espaciados uniformemente con valores que van desde 0 hasta 2 y el tamaño de la matriz es 5 filas
espacio2=np.linspace(0,2,5)
print(espacio2)
print()

# Conocer las dimensiones de una matriz
a=np.array([(1,2,3), (4,5,6)])
print(a.ndim)
print()

# conocer el tipo de datos que almacena una matriz
a=np.array([(1,2,3), (4,5,6)])
print(a.dtype)
print()

# conocer el tamaño y forma de la matriz
a=np.array([(1,2,3,4,5,6)])
print(a.size) #tamaño matriz
print(a.shape) #forma de matriz
print()

# Extraer un solo valor de la matriz
a=np.array([(1,2,3), (4,5,6)])
print(a[0,2])
print()

# Extraer todos los valores de todas las filas ubicadas en la columna 3
a=np.array([(1,2,3), (4,5,6)])
print(a[0:,2])
print()

# Econtrar el minimo, maximo y la suma de una matriz
a=np.array([1,2,3])
print("El minimo de la matriz es: ",a.min())
print(a.max())
print(a.sum())
print()

# Calcular la raiz cuadrada y la desviacion estandar de una matriz
a=np.array([(1,2,3), (4,5,6)])
print(np.sqrt(a))
print(np.std(a))
print()

# Calcular la multiplicacion, division, suma y resta de dos matrices
a=np.array([(1,2,3,4), (5,6,7,8)])
b=np.array([(1,2,3,4), (5,6,7,8)])
print(a*b)
print()
print(a/b)
print()
print(a+b)
print()
print(a-b)




