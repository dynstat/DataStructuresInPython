# Adjacent matrix representation of graph in Python

class Graph:
    def __init__(self, size):
        self.matrix = []
        # [[0, 0, 0, 0, 0],
        #  [0, 0, 0, 0, 0],
        #  [0, 0, 0, 0, 0],
        #  [0, 0, 0, 0, 0],
        #  [0, 0, 0, 0, 0]]
        for i in range(size):
            khali_list = []
            for j in range(size):
                khali_list.append(0)
            self.matrix.append(khali_list)
        # print(self.matrix)

    def print_graph(self):
        for i in self.matrix:
            print(i)

        # print(self.matrix)

    def add_edge(self, n1, n2):
        self.matrix[n1][n2] = 1
        self.matrix[n2][n1] = 1

    def remove_edge(self, edge_to_del: tuple):
        n1, n2 = edge_to_del
        self.matrix[n1][n2] = 0
        self.matrix[n2][n1] = 0


def main():
    g1 = Graph(4)
    g1.print_graph()
    edges = [(1, 0), (0, 2), (0, 3), (1, 2)]
    # g1.add_edge(1, 0)
    # g1.add_edge(0, 2)
    # g1.add_edge(0, 3)
    # g1.add_edge(1, 2)

    for (i, j) in edges:
        g1.add_edge(i, j)

    g1.print_graph()


if __name__ == "__main__":
    main()
