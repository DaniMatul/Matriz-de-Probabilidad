import numpy as np


def main():
    matriz_probabilidad = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
    matriz_x = [[0],
                [0],
                [0]]

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

        elif option == '2':
            print('Ingrese la clave: ')
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

        elif option == '4':
            break

        else:
            print('Esa opcion no esta disponible')


main()
