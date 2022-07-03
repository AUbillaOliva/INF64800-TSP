"""

Trabajo 2 - Análisis de Algoritmos - TSP

Problema del Viajante (TSP)
Integrantes:
- Maximiliano Olave
- Álvaro Ubilla

Sección: 301

Algoritmos utilizados:
- Programación Dinámica
- Algoritmo Voraz

"""

import sys
import dinamic
import voracious

if __name__ == '__main__':
    print('1. Programación dinamica')
    print('2. Programación voraz')
    
    opt = int(input("Selecciona una opcion: "))
    
    if opt == 1:
        dinamic.main()
    else: 
        voracious.main()