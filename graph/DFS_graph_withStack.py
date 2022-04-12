# DFS using Stack
class vtx:
    def __init__(self, name):
        self.vtx_name = name
        self.edges = []

    def __repr__(self) -> str:
        return f"{self.name}"


class Edge:
    def __init__(self, vertex_from, vertex_to, weight):
        self.vtx_from = vertex_from
        self.vtx_to = vertex_to
        self.wght = weight

    def __repr__(self) -> str:
        return f"{self.vtx_from},{self.vtx_to}"


class Graph:
    def __init__(self, vertexes: list = None, edges: list = None):
        if vertexes is None:
            vertexes = []
        if edges is None:
            edges = []
        self.vtxts = vertexes
        self.edges = edges
        self.visited: set = set()
        self.graph: dict = {}
        for v in self.vtxts:
            self.graph[v] = list()
        for v1, v2 in self.edges:
            self.graph[v1].append(v2)

    # Method for DFS traversal (using stack)
    def dfs(self):
        s = [list(self.graph.keys())[0]]
        while s:
            top = s.pop()
            if top not in self.visited:
                print(top, end=" ")
                self.visited.add(top)
            for n in self.graph[top]:
                if n not in self.visited:
                    s.append(n)


def dfs_global(some_graph: dict):
    # print(some_graph)
    # print(list(some_graph.keys())[0])
    stack = [list(some_graph.keys())[0]]
    # print(list(some_graph.keys())[0])
    length = len(stack)
    # for vx, edge_list in some_graph.items():
    visited = set()
    while stack:
        top = stack.pop()
        if top not in visited:
            print(top, end=" ")
        visited.add(top)
        neighbors_list = some_graph[top]
        for neighbor in neighbors_list:
            if neighbor not in visited:
                # inserting on the top of the stack
                # Or by python slicing stack[:0] = neighbor
                stack.append(neighbor)


if __name__ == "__main__":
    graph_elements = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a", "d"],
        "d": ["e"],
        "e": ["d"]
    }
    print("Using global function: ", end="")
    traverse_graph(graph_elements)
    print()
    # or by creating an object while passing a graph in it
    g1 = Graph(['a', 'b', 'c', 'd', 'e'], [
               ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'd'), ('c', 'a'), ('c', 'd'), ('d', 'e'), ('e', 'd')])
    print("Using class method dfs: ", end="")
    g1.dfs()
