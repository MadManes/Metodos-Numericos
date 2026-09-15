import dif_divididas

def inewton(x, fun, a):
    p_n = 0
    n = len(x)  # la posición n va a representar la diferencia de orden

    diferencias = dif_divididas(x, fun)
    puntos = []

    for i in range(n):
        if i == 0: puntos.append(1)
        else: puntos.append(puntos[i-1] * (a - x[i]))
        p_n += diferencias[i][0] * puntos[i]

    print(f'PN ---> {p_n}')

    return p_n