def dfs(nodo, grafo, searched, componentR):
    componentR.append(nodo)  # ir agregando los nodos que pertenecen al componente conectado
    searched[nodo] = True  # marcar al nodo como visitado
    print(searched)
    print('Vecinos de', nodo, ':', grafo[nodo])  # qué vecinos tiene el nodo

    # Recorrer los nodos adyacentes del nodo dado
    for vecino in grafo[nodo]:
        if not searched[vecino]:  # verificar que el nodo adyacente no está marcado como searched
            dfs(vecino, grafo, searched, componentR)  # llamada recursiva DFS
            print('Finaliza', vecino)
            print('Vuelve a', nodo)
            print()


graph = {
    0: [2, 1, 5],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [5, 4, 2],
    4: [3, 2],
    5: [3, 0]
}

nodoS = 0  # nodo start

# NUM
searched = [False] * len(graph)  # Al iniciar ningún nodo del graph ha sido visitado
print(searched)
componentR = []  # Lista para almacenar los nodos que pertenecen al componente conectado

dfs(nodoS, graph, searched, componentR)  # Dado el nodo start, aplicar DFS
print(f"La búsqueda DFS es: {componentR}")  # Imprimir los nodos que pertenecen al componente conectado
