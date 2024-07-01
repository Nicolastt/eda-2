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
    },
    'FIN': {}  # ! MUY IMPORTANTE
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
        break  # Detener el proceso si alcanzamos 'FIN'

    cost = costs[node]
    neighbors = graph[node]
    for n, weight in neighbors.items():
        new_cost = cost + weight
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


# Mostrar los resultados
print("Costos mínimos:")
for node in costs:
    print(f"{node}: {costs[node]}")

print("\nPadres:")
for node in parents:
    print(f"{node}: {parents[node]}")

# Reconstruir el camino más corto desde START hasta FIN
path = []
step = 'FIN'
while step != 'START':
    path.append(step)
    step = parents[step]
path.append('START')
path.reverse()
print("\nCamino más corto:")
print(path)
