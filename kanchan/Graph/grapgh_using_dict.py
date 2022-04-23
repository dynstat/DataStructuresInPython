# creating class of graph
class graph:
    def __init__(self, graph_element: dict = {}):
        self.graph = graph_element

    def show_edges(self):
        edge_ki_list = []
        for key, val in self.graph.items():
            for value in val:
                if (value, key) not in edge_ki_list:
                    edge_ki_list.append((key, value))
        return edge_ki_list
    # method to add edges
    def add_edges(self, edges: tuple = None):  # (f,g)
        v1, v2 = edges
        if v1 not in self.graph:
            self.graph[v1] = []
        if v2 not in self.graph:
            self.graph[v2] = []
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)
        if v1 not in self.graph[v2]:
            self.graph[v2].append(v1)


if __name__ == "__main__":
    graph_ele = {"a": ["b", "c"],
                 "b": ["a", "d"],
                 "c": ["a", "d"],
                 "d": ["e"],
                 "e": ["d"]}

    g1 = graph(graph_ele)
    print(g1.show_edges())
    g1.add_edges(("f", "g"))
    print(g1.show_edges())
