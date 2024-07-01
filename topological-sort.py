def indegree(nodo, grafo):
    return sum(nodo in adj for adj in grafo.values())


def topological_sort(grafo):
    top_sorted = []  # Lista para almacenar los nodos ordenados topológicamente
    ready = []  # Lista para almacenar los nodos listos para ser procesados
    incount = {}

    for nodo in grafo.keys():
        incount[nodo] = indegree(nodo, grafo)
        if incount[nodo] == 0:
            ready.append(nodo)
        print("Indegree", incount)
        print()
        print("Ready", ready)

    while len(ready) > 0:
        nodo = ready.pop()
        print("Nodo para usarse: ", nodo)
        top_sorted.append(nodo)
        for vecino in grafo[nodo]:
            print(vecino, ":", incount[vecino], " - 1")
            incount[vecino] -= 1
            if incount[vecino] == 0:
                ready.append(vecino)
        print("Ready", ready)

    print("Orden Topológico:", top_sorted)

grafo = {
    'A': ['B', 'C'],
    'B': ['E', 'G'],
    'C': [],
    'D': ['B', 'E', 'I'],
    'E': ['G'],
    'F': ['E','I'],
    'G': ['H'],
    'H': [],
    'I': ['H']
}

topological_sort(grafo)
