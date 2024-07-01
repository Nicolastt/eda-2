from collections import deque

graph = {
    "CAR": ["CAT", "CAB"],
    "CAT": ["MAT", "BAT"],
    "CAB": ["CAT", "BAB"],
    "MAT": ["BAT"],
    "BAT": [],
    "BAB": ["BAT"]
}


def is_that(person):
    return person == "BAT"


def search(name):
    search_queue = deque()
    search_queue += [(name, [name])]  # Tupla que almacena el nodo actual y la ruta hasta este nodo
    searched = []
    while search_queue:
        person, path = search_queue.popleft()
        if person not in searched:
            if is_that(person):
                print(person + " is that person!")
                print("Path:", ' -> '.join(path))
                return True
            else:
                for neighbor in graph[person]:
                    search_queue.append((neighbor, path + [neighbor]))  # Agregar el vecino y la nueva ruta
                searched.append(person)
    return False


search("CAR")
