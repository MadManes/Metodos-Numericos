import numpy as np

# Interpolación de Lagrange
def polinomios_base_lagrange(x_datos, x_val):
    n = len(x_datos)
    x_val = np.atleast_1d(n, len(x_val))
    polinomios = np.zeros(n, len(x_val))

    for i in range(n):
        numerador = 1
        denominador = 1
        for j in range(n):
            if i != j:
                numerador *= (x_val - x_datos[j])
                denominador *= (x_datos[i] - x_datos[j])

        polinomios[i,:] = numerador / denominador

    return polinomios

def lagrange(x_datos, y_datos, x_val):
    polinomios = polinomios_base_lagrange(x_datos, x_val)

    return np.sum(y_datos * polinomios, axis=0)



# Forma interpolante de Newton, donde x es la tupla de los x0,x1,...,xn
# y fun es la función a interpolar.

def funcion(x):
    return 1/x

def inewton(x, fun, a):
    p_n = 0
    n = len(x)  # la posición n va a representar la diferencia de orden

    diferencias = dif_divididas(x, fun)
    puntos = []

    for i in range(n):
        if i == 0: puntos.append(1)
        else: puntos.append(puntos[i-1] * (a - x[i]))
        p_n += diferencias[i][0] * puntos[i]

    #print(f'PN ---> {p_n}')

    return p_n

def dif_divididas(x, fun):
    difs = []        # las diferencias divididas que van a servir para armar p
    orden = len(x)   # el indice va a representar la diferencia de orden
    matriz_ordenes = [[] for i in range(orden)]

    # Caso base, cuando tengo el último término de las dif. divididas
    #if matriz_ordenes[-1] and matriz_ordenes[-1][1] == 0:
    #    print("...")


    if not difs:
        for i in range(orden):
            matriz_ordenes[0].append(fun(x[i]))

    #print("...")
    for i in range(orden):
    #    print(f'\n------------------\n{i+1}° Columna: \n')
        if matriz_ordenes[i]:
    #        print("columna completada")
            continue
        else:
            filas = orden - i
    #        print(f'FILAS {filas}')
            for j in range(orden):
                ## para orden 2 es la cantidad de columna 1 - 1
                ## para orden 3 es la cantidad de columna 2 - 1
                ## etcetera
                if j < filas:
                    x_sig = matriz_ordenes[(i-1)][j+1]
                    x_ant = matriz_ordenes[(i-1)][j]

                    if i < orden - 1:
    #                    print(f'f(x_i siguiente): {x_sig}')
    #                    print(f'f(x_i): {x_ant}')
    #                    print(f'Denominador: {x[i+j]} - {x[i+j-1]} = {x[i+j] - x[i+j-1]}')
                        diferencia = round(((x_sig - x_ant) /
                                      ((x[j+1]) -
                                       (x[j]))), 2)
                        
                        #print(f'Diferencia: {diferencia}')

                        matriz_ordenes[i].append(round(diferencia, 2))
                    else:
                        diferencia = ((x_sig - x_ant) /
                                      ((x[-1]) -
                                       (x[0])))
                        matriz_ordenes[i].append(round(diferencia, 2))

                        #print(f'Diferencia: {diferencia}')
                else:
                    matriz_ordenes[i].append(0)

    return matriz_ordenes

def polinomio_newton(x, fun, a):
    diferencias = dif_divididas(x, fun)

    p = 0
    producto = 1

    for i in range(len(x)):
        if i > 0:
            producto *= (a - x[i-1])

        p += diferencias[i][0] * producto

    return p

#print(dif_divididas((2, 2.5, 4), funcion))
#print(inewton((2, 2.5, 4, 6, 6.6, 7, 9, 12, 13.5), funcion, 7))
#print(inewton((2, 2.5, 4), funcion, 3))
