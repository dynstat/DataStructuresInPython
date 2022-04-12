# creating a class of node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# creating a class of graph
class graph:
    def __init__(self, graph_element):
        self.graph = graph_element

    def bfs(self, graph):
        q = list(self.graph.keys())[0]
        visited_list = []
        while q:
            var_first = q.pop(0)
            if var_first not in visited_list:
                visited_list.append(var_first)
                print(var_first)
            for val in self.graph:
                q.append(val)


if __name__ == "__main__":
    graph_ele = {"a": ["b", "c"],
                 "b": ["a", "d"],
                 "c": ["a", "d"],
                 "d": ["e"],
                 "e": ["d"]}
