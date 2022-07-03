# INF64800 - Análisis de Algoritmos

Trabajo de investigación y aplicación de la asignatura Análisis de Algoritmos `INF64800`.
El problema del trabajo consiste en implementar en 2 algoritmos escogidos, el problema de el viajero (`TSP`)

**Autores**:

- Álvaro Ubilla
- Maximiliano Olave

---

Implementar el algoritmo del problema del viajero `TSP` con diastancias de ciudades chilenas.

Utilizar 2 algoritmos escogidos:

- Programación Dinámica
- Algoritmos Voraz

## Problema TSP

El problema TSP (Traveler Sales Problem) responde
a la siguiente pregunta: Dada una lista de ciudades y las distancias entre cada par de ellas, ¿cuál
es la ruta más corta posible que visita cada ciudad exactamente una vez y regresa a la ciudad
origen? Este es un problema NP-duro dentro en la optimización combinatoria, muy importante
en la investigación de operaciones y en la ciencia de la computación.
El problema fue formulado por primera vez en 1930 y es uno de los problemas de optimización
más estudiados. Es usado como prueba para muchos métodos de optimización. Aunque el
problema es computacionalmente complejo, una gran cantidad de heurísticas y métodos
exactos son conocidos, de manera que, algunas instancias desde cien hasta miles de ciudades
pueden ser resueltas.
El TSP tiene diversas aplicaciones aún en su formulación más simple, tales como: la planificación,
la logística y en la fabricación de microchips. Un poco modificado, aparece como: un sub-problema en muchas áreas, como en la secuencia de ADN. En esta aplicación, el concepto de
“ciudad” representa, por ejemplo: clientes, puntos de soldadura o fragmentos de ADN y el
concepto de “distancia” representa el tiempo de viaje o costo, o una medida de similitud entre
los fragmentos de ADN. En muchas aplicaciones, restricciones adicionales como el límite de
recurso o las ventanas de tiempo hacen el problema considerablemente difícil. El TSP es un caso
especial de los Problemas del Comprador Viajante (travelling purchaser problem).
En la teoría de la complejidad computacional, la versión de decisión del TSP (donde, dado un
largo “L”, la tarea es decidir cuál grafo tiene un camino menor que L) pertenece a la clase de los
problemas NP-completos. Por tanto, es probable que en el caso peor el tiempo de ejecución
para cualquier algoritmo que resuelva el TSP aumente de forma exponencial con respecto al
número de ciudades.
Historia
El origen de los problemas del agente viajero no está claro. Una guía para agentes viajeros de
1832 menciona el problema e incluye ejemplos de viajes a través de Alemania y Suiza, pero no
contiene un tratamiento matemático del mismo.
El problema del agente viajero fue definido en los años 1800s por el matemático irlandés W. R.
Hamilton y por el matemático británico Thomas Kirkman. El Juego Icosian de Hamilton fue un
puzzle recreativo basado en encontrar un ciclo de Hamilton. Todo parece indicar que la forma
general del TSP fue estudiada, por primera vez por matemáticos en Viena y Harvard, durante los
años 1930s.
Destacándose Karl Menger, quien definió los problemas, considerando el obvio algoritmo de
fuerza bruta, y observando la no optimalidad de la heurística de vecinos más cercanos:
Denotamos por “Problema del Mensajero” (dado que en la práctica esta pregunta puede
resolverse por cada cartero, aunque puede ser resuelta por varios viajeros) la pregunta es
encontrar, para un conjunto finito de puntos de los cuales se conocen las distancias entre cada
par, el camino más corto entre estos puntos. Por supuesto, el problema es resuelto por un
conjunto finito de intentos. La regla que se debe seguir es que desde el punto inicial se va al
punto más cercano a este, de ahí a su más cercano y así sucesivamente, en general este algoritmono retorna la ruta más corta.

## Algoritmos

### Programación dinamica

La Programación Dinámica es un método de optimización de extraordinaria versatilidad. Si bien fue desarrollada especialmente para la resolución de problemas en
Procesos de Decisión en Múltiples Pasos, diferentes investigaciones han mostrado que
las mismas ideas pueden utilizarse en otro tipo de problemas de matemática aplicada, e incluso pueden ser útiles en el planteo de algunas cuestiones teóricas. Habiendo
surgido en los inicios de la época de las computadoras, la Programación Dinámica
fue, además, concebida con un ojo puesto en esta potente herramienta. La Ecuación
Funcional que se obtiene, para cada problema, a través del uso del Principio de Optimalidad de Bellman permite, con mayor o menor esfuerzo dependiendo del caso,
establecer una recurrencia que es, en sí misma, un algoritmo que resuelve el problema
en cuestión

[Maurette, M., & Ojea, I. (2006). Programación Dinámica. Universidad de Buenos Aires Sitio Web: http://cms. dm. uba. ar/materias/1ercuat2009/optimizacion/Maurette_Ojea. pdf.](http://cms.dm.uba.ar/materias/1ercuat2009/optimizacion/Maurette_Ojea.pdf)

#### Aplicación a TSP - Programación dinamica

Este problema se puede resolver utilizando el algoritmo de programación dinamica. A continuación, se muestran los pasos:

- Crear dos data holder primarios: Una lista que contiene los índices de las ciudades y otra que contiene las distancias entre las ciudades con respecto a la lista anterior.
- Objetos que contiene el indice de la ciudad mas una lista con las distancias a otras ciudades.
- Una matriz que contiene todos las distancias minimas entre las ciudades.
- Realizar un recorrido en la matriz de adyacencia dada y obtenga los distancias minimas en la lista del objeto
- Obtener la distancia minima entre las listas usando recursividad
- Genere el ciclo de ruta mínimo utilizando el paso anterior y devuelva allí el costo mínimo.

---

### Programación voraz

Es una estrategia de búsqueda por la cual se sigue una heurística consistente en elegir la opción óptima en cada paso local con la esperanza de llegar a una solución general óptima. Este esquema algorítmico es el que menos dificultades plantea a la hora de diseñar y comprobar su funcionamiento. Normalmente se aplica a los problemas de optimización.
Toman decisiones en función de la información que está disponible en cada momento. Una vez tomada la decisión, ésta no vuelve a replantearse en el futuro. Suelen ser rápidos y fáciles de implementar. No siempre garantizan alcanzar la solución óptima.
El enfoque “greedy” no nos garantiza obtener soluciones óptimas. Por lo tanto, siempre habrá que estudiar la corrección del algoritmo para demostrar si las soluciones obtenidas son óptimas o no.

#### Aplicación a TSP - Programación voraz

Este problema se puede resolver utilizando la técnica Greedy (Algoritmo Voraz). A continuación, se muestran los pasos:

- Cree dos data holders primarios: Una lista que contiene los índices de las ciudades en términos de la matriz de entrada de distancias entre ciudades.
- Matriz de resultados que tendrá todas las ciudades que se pueden mostrar en la consola de cualquier manera.
- Realice un recorrido en la matriz de adyacencia dada TSP [ ] [ ] para toda la ciudad y si el costo de llegar a cualquier ciudad desde la ciudad actual es menor que el costo actual, actualice el costo.
- Genere el ciclo de ruta mínimo utilizando el paso anterior y devuelva allí el costo mínimo.

## Conclusiones

Como conclusión, ambos algoritmos son utilizados en ambientes de optimización, generalmente para disminuir los tiempos de ejecución de los algoritmos evaluados. En este particular proyecto, podemos observar que ambos algoritmos puedes ser utilizados para obtener la ruta mas corta entre distintas ciudades de chile. Sin embargo ambos algoritmos se ejecutan de distinta forma, lo que genera resultados distintos a la hora de procesar los datos del problema.

También debemos señalar que:

- La programación dinámica, al usar una matriz para guardar los valores que va calculando, está limitada por el tamaño de la memoria de nuestro ordenador.
