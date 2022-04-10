# BFS traversal in the graph using queue (deque from the collections package)

from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


class Graph:
    def __init__(self, someGraph: dict) -> None:
        self.graph: dict = someGraph
        self.visited = set()  # empty set to store visited nodes
        # self.parent = {}
        # self.level = {}

    def bfs(self):
        # queue created with first key (Node) of the graph dictionary in it.
        q = deque([list(self.graph.keys())[0]])
        while q:
            first = q.popleft()
            # checking wether popped item is already visited or not, before printing.
            if first not in self.visited:
                print(first)
                self.visited.add(first)
            # looping through all the neighbour nodes
            for n in self.graph[first]:
                if n not in self.visited:
                    # appending the neighbour nodes at the end of queue
                    q.append(n)


if __name__ == "__main__":
    my_graph = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a", "d"],
        "d": ["e"],
        "e": ["d"]
    }

    graph_obj = Graph(my_graph)
    graph_obj.bfs()
