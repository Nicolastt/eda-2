from collections import deque

graph_G = {
    0: [2, 1, 5],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [5, 4, 2],
    4: [3, 2],
    5: [3, 0]
}


def bfs_tree(graph, start):
    # Estructura para almacenar el árbol BFS
    tree = {}
    # Conjunto para mantener un registro de nodos visitados
    visited = set()
    # Iniciar la cola de búsqueda con el nodo de inicio y su padre (None para el nodo raíz)
    queue = deque([(start, None)])

    while queue:
        node, parent = queue.popleft()
        if node not in visited:
            visited.add(node)
            if parent is not None:
                tree.setdefault(parent, []).append(node)  # Agregar el nodo como hijo del padre en el árbol
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # Agregar vecinos a la cola con el nodo actual como padre
                    queue.append((neighbor, node))
    return tree


start_node = 0
bfs_tree_result = bfs_tree(graph_G, start_node)
print("BFS Tree from node", start_node, ":", bfs_tree_result)
