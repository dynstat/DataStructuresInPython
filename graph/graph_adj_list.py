class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size

    def add_edge(self, src, des):  # src = 0, des = 1
        adj_node = Node(des)
        adj_node.next = self.array[src]
        self.array[src] = adj_node

        adj_node = Node(src)
        adj_node.next = self.array[des]
        self.array[des] = adj_node

    def print_graph(self):
        for i in range(self.size):
            print(f"Vertex {i}:", end="")
            temp = self.array[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    g1 = Graph(4)
    g1.print_graph()

    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)

    g1. print_graph()
