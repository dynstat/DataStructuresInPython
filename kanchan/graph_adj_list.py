class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None

    def __repr__(self):
        return self.vertex


class graph:
    def __init__(self, vertex_size):
        self.array = [None]*vertex_size

    def add_edges(self, src, des):
        new_vertex = Node(des)
        new_vertex.next = self.array[src]
        self.array[src] = new_vertex

        new_vertex = Node(src)
        new_vertex.next = self.array[des]
        self.array[des] = new_vertex

    def print_edges(self):
        count = 0
        for i in self.array:

            temp = i
            print(f"vertex {count}", end="")
            while temp is not None:
                print(f"--->{temp.vertex}", end="")
                temp = temp.next
            print("")
            count = count+1


if __name__ == "__main__":
    n1 = Node(0)
    n1 = Node(1)
    n1 = Node(2)
    n1 = Node(3)

    g1 = graph(4)
    g1.add_edges(0, 1)
    g1.add_edges(0, 2)
    g1.add_edges(0, 3)
    g1.add_edges(1, 2)

    g1.print_edges()
