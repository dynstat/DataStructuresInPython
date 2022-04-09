# BFS traversal in the graph using queue (deque from the collections package)

from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None


class Graph:
    def __init__(self, someGraph: Node) -> None:
        self.graph = someGraph
        self.visited = set()  # empty set to store visited nodes
        # self.parent = {}
        # self.level = {}

    def bfs(self):
        q = deque([self.graph])
        while q:
            first = q.popleft()
            if first not in self.visited:
                print(first)
            self.visited.add(first)
