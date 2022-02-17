#  To implement a graph if we used C language (i.e. without using a dictionary)
# let the nodes in the graph looks like :
# "a": ["b", "c"],
# "b": ["a", "d"],
# "c": ["a", "d"],
# "d": ["e"],
# "e": ["d"]
# Now, since we have to use array like data structure as C doesn't have a dictionary

#  Create a Graph by manually adding the nodes and edges
#  Put the values of nodes as integer only
class Graph:
    def __init__(self, vtx, edges) -> None:  # edges consists of tuple of tuples consisting of the edges info (vertex1, vertex2) and the vtx consists of number of vertexs or nodes i.e if vtx = 5 then ==> nodes must be (0,1,2,3,4)
        self.V = vtx
        self.E = edges
        # For the adjacency list method, we need to create a list of lists which can consist all the adjacent nodes of the node (here the index number of the self.arr is considered as the Node itself)
        # Note: if the nodes have some name, then we should either map these names as the numbers or we will have to use a different approach.
        self.arr = [[] for _ in range(self.V)]
        # as we know that the edges have two values.. i.e nodes, so take the node values in vx1, vx2.
        # append the adjacent nodes into the list.
        for vx1, vx2 in edges:
            self.arr[vx1].append(vx2)
            self.arr[vx2].append(vx1)
        # print(self.arr)

    # repr() function is called automatically when we try to access the object directly
    # showing all the nodes and their adjacent nodes in this
    def __repr__(self) -> str:
        return "\n".join([f"{index} : {val}" for index, val in enumerate(self.arr)])

    # str() function is called when the object is printed as a string (to make it more like a human readable format)
    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    g1 = Graph(4, ((1, 2), (0, 3), (0, 2)))
    print(g1)
