import json
import sys
import copy

file = open('data.json')
file_data = json.load(file)

distances = file_data['DISTANCES']
city_names = file_data['CITY_NAMES']

matrix = distances
data = list(range(1, len(city_names)+1))

n = len(data)
all_sets = []
g = {}
p = []

def main():
    for i in range(1, n):
        g[i + 1, ()] = matrix[i][0]

    minimum(1, (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

    print('\n\nSolución: {chaiten, ', end='')
    current = p.pop()
    print(city_names[current[1][0]-1], end=', ')
    for i in range(n - 2):
        for tmp in p:
            if tuple(current[1]) == tmp[0]:
                current = tmp
                city_name = city_names[current[1][0]-1]
                print(city_name , end=', ')
                break
    print('chaiten}\n\n')
    return


def minimum(k, a):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    # minimun value
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
    sys.exit(0)
