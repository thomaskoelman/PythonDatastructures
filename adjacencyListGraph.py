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

    def for_each_node(self, op):
        for n in self.nodes():
            op(n)

    def for_each_edge_of_node(self, node, op):
        for e in self.neighbours(node):
            op(e)

    def dft(self, root_discovered, node_discovered, node_processed, edge_discovered, edge_processed, edge_bumped,
            roots=[]):
        visited = [False] * self.order()

        def has_visited(n):
            return visited[n]

        def dft_component(root):
            def expand(from_node, to_node):
                if (has_visited(to_node)):
                    if (not edge_bumped(from_node, to_node)):
                        return False
                else:
                    if (not (edge_discovered(from_node, to_node) and dft_rec(to_node) and edge_processed(from_node, to_node))):
                        return False

            def dft_rec(from_node):
                if (not node_discovered(from_node)): return False
                visited[from_node] = True
                self.for_each_edge_of_node(from_node, (lambda to_node: expand(from_node, to_node)))
                if (not node_processed(from_node)): return from_node
            if (not has_visited(root)):
                if (root_discovered(root)):
                    dft_rec(root)
                else:
                    return False

        if not roots:
            self.for_each_node(dft_component)
        else:
            for root in roots:
                dft_component(root)

    def root_nop(self, root):
        return True
    def node_nop(self, node):
        return True
    def edge_nop(self, from_node, to_node):
        return True

    def is_connected_component(self):
        count = 0
        def incr():
            nonlocal count
            count = count + 1
            return True
        self.dft(lambda root: incr(), self.node_nop, self.node_nop, self.edge_nop, self.edge_nop, self.edge_nop)
        return (count == 1)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
def root_discovered(root):
    print("new root: ", str(root))
    return True
def node_discovered(node):
    print("new node: ", str(node))
    return True
def node_processed(node):
    print("node processed: ", str(node))
    return True
def edge_discovered(from_node, to_node):
    print("edge discovered from ", str(from_node), " to ", str(to_node))
    return True
def edge_processed(from_node, to_node):
    print("edge processed from ", str(from_node), " to ", str(to_node))
    return True
def edge_bumped(from_node, to_node):
    print("edge bumped from ", str(from_node), " to ", str(to_node))
    return True
g.dft(root_discovered, node_discovered, node_processed, edge_discovered, edge_processed, edge_bumped)
