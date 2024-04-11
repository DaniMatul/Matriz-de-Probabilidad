import numpy as np


def transpuesta_matriz_probabilidad(matriz_probabilidad):
    matriz_tranpuesta = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
    for a in range(3):
        for b in range(3):
            matriz_tranpuesta[a][b] = (matriz_probabilidad[b][a])

    return matriz_tranpuesta


def multiplicar_probabilidad(matriz_probabilidad_t, matriz_x, cantidad_veces):
    if cantidad_veces == 1:
        matriz_resultado = np.dot(matriz_probabilidad_t, matriz_x)
        return matriz_resultado
    else:
        matriz_primera = np.dot(matriz_probabilidad_t, matriz_x)
        ma = matriz_primera
        matriz_general = [matriz_primera]
        for a in range(cantidad_veces):
            matriz_general = np.dot(matriz_probabilidad_t, ma)
            ma = matriz_general

        return matriz_general

def multiplicar_porcentaje(matriz_general):
    for a in range(3):
        for b in range(3):
            matriz_general[a][b] = matriz_general[a][b] * 100

    return matriz_general


def main():
    matriz_probabilidad = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
    matriz_x = [[0],
                [0],
                [0]]

    matriz_probabilidad_t = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]

    while True:
        print('--- Menu ---' '\n1) Ingresar la matriz de probabilidad \n2) Ingresar la matriz x '
              '\n3) Cantidad de veces a multiplicar \n4) Salir')
        option = input('Que decea realizar: ')

        if option == '1':
            print('Ingrese la clave: ')
            for i in range(3):
                for j in range(3):
                    # Solicitar al usuario que ingrese un número
                    numero = float(input(f"Ingrese el número para la posición [{i}][{j}]: "))
                    # Asignar el número ingresado a la posición actual de la matriz
                    matriz_probabilidad[i][j] = numero
            # Imprimir la matriz
            print('Tu matriz de probabilidad es: ')
            for fila in matriz_probabilidad:
                print(fila)

            # Hacer transpuesta
            matriz_probabilidad_t = transpuesta_matriz_probabilidad(matriz_probabilidad)
            print("Esta es tu matriz de transición")
            for fila in matriz_probabilidad_t:
                print(fila)

        elif option == '2':
            print('Ingrese la matriz x: ')
            for i in range(3):
                for j in range(1):
                    # Solicitar al usuario que ingrese un número
                    numero = float(input(f"Ingrese el número para la posición [{i}][{j}]: "))
                    # Asignar el número ingresado a la posición actual de la matriz
                    matriz_x[i][j] = numero
            # Imprimir la matriz
            print('Tu matriz x es: ')
            for fila in matriz_x:
                print(fila)

        elif option == '3':
            cantidad = int(input('Ingrese la cantidad de veces que va a multiplicar: '))
            resultado = multiplicar_probabilidad(matriz_probabilidad_t, matriz_x, cantidad)
            print(resultado)

        elif option == '4':
            break

        else:
            print('Esa opcion no esta disponible')


main()




