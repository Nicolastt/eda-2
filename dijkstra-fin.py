graph = {
    'START': {
        'A': 6,
        'B': 2
    },
    'A': {
        'FIN': 1
    },
    'B': {
        'A': 3,
        'FIN': 5
    }
}

infinity = float('inf')
costs = {
    'A': 6,
    'B': 2,
    'FIN': infinity
}

parents = {
    'A': 'START',
    'B': 'START',
    'FIN': None
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    if node == 'FIN':
        break  # Si alcanzamos el nodo FIN, detenemos el proceso

    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# Reconstruir el camino más corto desde START hasta FIN
path = []
step = 'FIN'
while step != 'START':
    path.append(step)
    step = parents[step]
path.append('START')
path.reverse()

print(f"El camino más barato desde START hasta FIN es: {' -> '.join(path)} con un costo de {costs['FIN']}")
