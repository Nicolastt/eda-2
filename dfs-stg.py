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


grafo_G = {
    "Start": ["A", "B", "C"],
    "A": ["B", "G"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["E", "F"],
    "E": ["F"],
    "F": [],
    "G": ["D"]
}

nodoS = "Start"  # nodo start
# STRING
searched = {nodo: False for nodo in grafo_G}  # al iniciar ningún nodo del graph ha sido visitado
componentR = []  # lista para almacenar los nodos que pertenecen al componente conectado

dfs(nodoS, grafo_G, searched, componentR)  # Dado el nodo start, aplicar DFS
print(f"La búsqueda DFS es: {componentR}")  # Imprimir los nodos que pertenecen al componente conectado
