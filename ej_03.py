import matplotlib.pyplot as plt 
import numpy as np
from prueba import inewton, polinomio_newton

'''
# Prueba
datos_x = [1, 2, 3, 4, 5]
datos_y = [2, 4, 9, 16, 25]

plt.plot(datos_x, datos_y, marker='o', color='blue', label='funcion')

plt.title('Gráfico')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True)
plt.legend()
plt.show()
'''

# Con lista de tuplas
#puntos = [(), (), (), (), ()]
#datos_x, datos_y = zip(*puntos)
#plt.plot(datos_x, datos_y, marker='o', color='blue', label='funcion')
#
#plt.title('Gráfico')
#plt.xlabel('Eje x')
#plt.ylabel('Eje y')
#plt.grid(True)
#plt.legend()
#plt.show()

'''      
## Generando puntos
# Generar puntos intermedios en ese rango
x = np.linspace(0.01, 5, 100)

# Crear la función
y = 1/x

# Crear el gráfico
plt.plot(x, y, color='purple', label='f(x) = 1/x')

# Imprimir gráfico
plt.title('Gráfico')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.show()'''


## Ejercicio 3

def funcion(x):
    return 1/x

puntos = []
x_int = []
puntos_int = []

for j in range(1, 101):    
    x = 24/25 + j/25
    y = funcion(x)    
    puntos.append((x,y))
    x_int.append(x)

for j in range(1, 101):
    y_int = polinomio_newton(x_int, funcion, x_int[j-1])
    puntos_int.append((x_int[j-1], y_int))
    if j < 10:
        print(f'Punto {puntos_int[j-1]}')

datos_x, datos_y = zip(*puntos)

plt.plot(datos_x, datos_y, color='purple', label='f(x) = 1/x')

plt.title('Ejercicio N°3')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.legend()
plt.show()

datos_x, datos_y = zip(*puntos_int)

plt.plot(datos_x, datos_y, color='purple', label='f(x) = 1/x (Interpolante de Newton)')

plt.title('Ejercicio N°3')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.legend()
plt.show()



# Ejemplo de la página de documentación de matplotlib
#t = np.arange(0., 5., 0.2)


#fig, ax = plt.subplots()             # Create a figure containing a single Axes.
#ax.plot(t, 1/t)                      # Plot some data on the Axes.
#plt.show()                           # Show the figure.