
# creating a class of node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# creating a class of graph
class graph:
    def __init__(self, graph_element):
        self.graph = graph_element

    # a method to traverse a graph using breadth first search
    def bfs(self):
        q = [list(self.graph.keys())[0]]

        visited_list = []
        while q:
            # since new items are added on the right of the present list (in queue),
            # we will have to pop the left most item, thats why we have used pop(0)
            var_first = q.pop(0)
            if var_first not in visited_list:
                visited_list.append(var_first)
                print(var_first)

            for val in self.graph[var_first]:
                if val not in visited_list:
                    q.append(val)

    # a method to traverse the graph in depth first search
    def dfs(self):
        stack = [list(self.graph.keys())[0]]
        visited = []
        while stack:
            # since new items are added on the right side of the present stack
            # we have to pop the right most item, that's why we have used pop()
            var_last = stack.pop()
            if var_last not in visited:
                visited.append(var_last)
                print(var_last)

            for val in self.graph[var_last]:
                if val not in visited:
                    stack.append(val)

# driver code
if __name__ == "__main__":
    graph_ele = {"a": ["b", "c"],
                 "b": ["a", "d"],
                 "c": ["a", "d"],
                 "d": ["e"],
                 "e": ["d"]}

    graph1 = graph(graph_ele)
    graph1.bfs()
    print('graph traversal using dfs')
    graph1.dfs()
