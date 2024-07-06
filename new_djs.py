def dijkstra(graph, start, end):
    infinity = float('inf')

    # Initialize the costs and parents dictionaries
    costs = {node: infinity for node in graph}
    costs[start] = 0

    parents = {node: None for node in graph}
    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = infinity
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
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    # Return results
    return costs, parents


def shortest_path(graph, start, end):
    costs, parents = dijkstra(graph, start, end)

    # Display minimum costs
    print("Costos mínimos:")
    for node in costs:
        print(f"{node}: {costs[node]}")

    # Display parents
    print("\nPadres:")
    for node in parents:
        print(f"{node}: {parents[node]}")

    # Reconstruct the shortest path
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents[step]
    path.reverse()

    print("\nCamino más corto:")
    print(path)


# Ejemplo de uso
graph = {
    'S': {'A': 4, 'B': 8, 'C': 16},
    'A': {'B': 3},
    'B': {'C': 7, 'F': 1},
    'C': {'D': 2},
    'D': {},
    'F': {'C': 5, 'D': 6},
}

shortest_path(graph, 'S', 'F')
