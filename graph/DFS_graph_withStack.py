# DFS using Stack

from typing import Dict, List


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
    def __init__(self, vertexes: List = [], edges: List = []):
        self.vtxts = vertexes
        self.edges = edges

    # Method for DFS traversal


def traverse_graph(some_graph: Dict):
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
            print(top)
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
    traverse_graph(graph_elements)
