class Graph:
    def __init__(self, directed=False, nodes=0):
        self.__is_directed = directed
        self.__storage = []
        self.__order = 0
        self.__nmbr_of_edges = 0
        self.__add_node(nodes)

    def __add_node(self, nmbr=1):
        for i in range(nmbr):
            self.__storage.append([])
            self.__order = self.__order + 1

    def add_edge(self, from_node, to_node):
        if (not self.is_adjacent(from_node, to_node)):
            self.__storage[from_node].append(to_node)
            self.__nmbr_of_edges = self.__nmbr_of_edges + 1
            if (not self.is_directed()):
                self.__storage[to_node].append(from_node)
        else:
            pass

    def delete_edge(self, from_node, to_node):
        if (self.is_adjacent(from_node, to_node)):
            self.__storage[from_node].remove(to_node)
            self.__nmbr_of_edges = self.__nmbr_of_edges - 1
            if (not self.is_directed()):
                self.__storage[to_node].remove(from_node)
        else:
            pass

    def is_directed(self):
        return self.__is_directed

    def order(self):
        return self.__order

    def nmbr_of_edges(self):
        return self.__nmbr_of_edges

    def nodes(self):
        return set(range(self.order()))

    def neighbours(self, node):
        return set(self.__storage[node])

    def is_adjacent(self, from_node, to_node):
        if self.__is_directed:
            return (to_node in self.__storage[from_node])
        else:
            return (to_node in self.__storage[from_node]) and (from_node in self.__storage[to_node])