graph = {
    'S': {'A': 4, 'B': 8, 'C': 16},
    'A': {'B': 3},
    'B': {'C': 7, 'F':1},
    'C': {'D': 2},
    'F': {'C': 5, 'D': 6},
}

infinity = float('inf')

costs = {
    'A': float('inf'),
    'B': float('inf'),
    'C': float('inf'),
    'D': float('inf'),
    'F': float('inf')
}

parents = {
    'S': None,
    'A': None,
    'B': None,
    'C': None,
    'D': None,
    'F': None
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
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
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
