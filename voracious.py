import json
from typing import DefaultDict


INT_MAX = 2147483647

# Funcion para encontrar el costo
# minimo de los caminos


def RutaMinima(tsp):
    sum = 0
    contador = 0
    j = 0
    i = 0
    min = INT_MAX
    ListaRuta = DefaultDict(int)

    # Iniciando en la ciudad 0
    ListaRuta[0] = 1
    ruta = [0] * len(tsp)

    # Atravieza la adyaciencia
    # MATRIZ tsp[][]
    while i < len(tsp) and j < len(tsp[i]):

        # Esquina de la matriz
        if contador >= len(tsp[i]) - 1:
            break

        # Si este camino no se visita,
        # y si el costo es menor entonces
        # actualiza el costo
        if j != i and (ListaRuta[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                ruta[contador] = j + 1

        j += 1

        # Revisa todos los caminos de
        # la n ciudad indexada
        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            ListaRuta[ruta[contador] - 1] = 1
            j = 0
            i = ruta[contador] - 1
            contador += 1

    # Actuliza la ultima ciudad en el array
    # desde la ciudad que hemos visitado
    i = ruta[contador - 1] - 1

    for j in range(len(tsp)):

        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            ruta[contador] = j + 1

    sum += min

    # Comienza del nodo de donde se termina.
    print("Minimum Cost is :", sum)


def main():
    file = open('data.json')
    file_data = json.load(file)

    distances = file_data['DISTANCES']
    # Entrada
    tsp = distances

    # Llamada a la funcion
    RutaMinima(tsp)


if __name__ == "__main__":
    main()
