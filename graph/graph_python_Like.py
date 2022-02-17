# Graph implementation in Python assuming that the nodes and edges are stored in a dictionary.

# Creating a Graph class
class Graph:
    # constructor function which takes graph elements and edges as a dictionary
    def __init__(self, graph_elem=None):
        self.graph = {} if graph_elem is None else graph_elem

    # Function to print the edges (without repeating)
    def show_edges(self):
        edges_list = []  # an empty list to store the edges data of all the nodes
        for key, value in self.graph.items():
            for val in value:
                if (val, key) not in edges_list:
                    edges_list.append((key, val))
        return edges_list


if __name__ == "__main__":
    # data of the graph in dictionary form
    graph_elements = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a", "d"],
        "d": ["e"],
        "e": ["d"]
    }
    g1 = Graph(graph_elem=graph_elements)
    print(g1.show_edges())
