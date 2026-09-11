def dif_divididas(x, fun):
    difs = []        # las diferencias divididas que van a servir para armar p
    orden = len(x)   # el indice va a representar la diferencia de orden
    matriz_ordenes = [[] for i in range(orden)]

    # Caso base, cuando tengo el último término de las dif. divididas
    if matriz_ordenes[-1] and matriz_ordenes[-1][1] == 0:
        print("...")


    if not difs:
        for i in range(orden):
            matriz_ordenes[0].append(fun(x[i]))

    print("...")
    for i in range(orden):
        print(f'\n------------------\n{i+1}° Columna: \n')
        if matriz_ordenes[i]:
            print("columna completada")
            continue
        else:
            filas = orden - i
            print(f'FILAS {filas}')
            for j in range(orden):
                ## para orden 2 es la cantidad de columna 1 - 1
                ## para orden 3 es la cantidad de columna 2 - 1
                ## etcetera
                if j < filas:
                    x_sig = matriz_ordenes[(i-1)][j+1]
                    x_ant = matriz_ordenes[(i-1)][j]

                    if i < orden - 1:
                        print(f'f(x_i siguiente): {x_sig}')
                        print(f'f(x_i): {x_ant}')
                        print(f'Denominador: {x[i+j]} - {x[i+j-1]} = {x[i+j] - x[i+j-1]}')
                        diferencia = round(((x_sig - x_ant) /
                                      ((x[j+1]) -
                                       (x[j]))), 2)
                        
                        print(f'Diferencia: {diferencia}')

                        matriz_ordenes[i].append(round(diferencia, 2))
                    else:
                        diferencia = ((x_sig - x_ant) /
                                      ((x[-1]) -
                                       (x[0])))
                        matriz_ordenes[i].append(round(diferencia, 2))

                        print(f'Diferencia: {diferencia}')
                else:
                    matriz_ordenes[i].append(0)

    return matriz_ordenes