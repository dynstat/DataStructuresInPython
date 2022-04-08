class graph:
    def __init__(self, size):
        self.matrix = []
        for _ in range(size):
            khali_list = []
            for _ in range(size):
                khali_list.append(0)
            self.matrix.append(khali_list)

    def print_matix(self):
        for i in self.matrix:
            print(i)

    def add_edge(self, n1, n2):
        self.matrix[n1][n2] = 1
        self.matrix[n2][n1] = 1

    def del_edge(self, edge: tuple):
        x, y = edge
        self.matrix[x][y] = 0
        self.matrix[y][x] = 0


graph1 = graph(4)
graph1.add_edge(1, 2)
graph1.print_matix()
graph1.del_edge((1, 2))
graph1.print_matix()
