# Basic weighted, undirected Graph representation


# creating a structure (class) of Node or vertex present in the graph
class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __repr__(self) -> str:
        return self.name


# creating the structure (or class) of an edge present in the graph
class Edge:
    def __init__(self, vertx_from, vertx_to, weight=None):
        self.weight = weight
        self.vtx_from = vertx_from
        self.vtx_to = vertx_to

    def __repr__(self) -> str:
        return f"({self.vtx_from}, {self.vtx_to})"


# Now, Creating the graph, which is basically made up of vertexes and the edges defined above
class Graph:
    def __init__(self, vertexs: list = [], edges: list = []):
        self.vtxs = vertexs
        self.edges = edges

    # A method to add a new node/vertex in the Graph
    def insert_vtx(self, new_vertex_name):
        # creating a new vertex using Vertex class
        new_vtx = Vertex(new_vertex_name)
        # Now, update the vertex list (self.vtxs) of the Graph
        self.vtxs.append(new_vtx)

    def insert_edge(self, vtx_from_name, vtx_to_name, new_edge_weight=None):
        from_found = None
        to_found = None

        # Checking through the entire list of existing edges, whether the "from" and "to" vertexes already exist or not.
        for vx in self.vtxs:
            if vtx_from_name == vx.name:
                from_found = vx

            if vtx_to_name == vx.name:
                to_found = vx
        # If any or both of the given vertexes were not found in the already existing list of vertexes, create a new one and append it into the self.vtxs list
        if from_found is None:
            from_found = Vertex(vtx_from_name)
            self.vtxs.append(from_found)
        if to_found is None:
            to_found = Vertex(vtx_to_name)
            self.vtxs.append(to_found)

        # Now that we have found or created the "from" and "to" vertexes, create a new edge using Edge class.
        new_edge = Edge(from_found, to_found, new_edge_weight)
        # Adding the new edge in the respective vertexes related to this edge
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)

        # Finally, Adding this new edge into the graph.edges attribute
        self.edges.append(new_edge)


# MAIN DRIVER CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # Given data
    given_cities = ["Delhi", "Pune", "Bangalore"]
    given_roads = [("Delhi", "Pune"), ("Pune", "Bangalore"),
                   ("Delhi", "Bangalore")]
    cities = []
    roads = []

    for c in given_cities:
        city = Vertex(c)
        cities.append(city)
    for c_fr, c_to in given_roads:
        road = Edge(c_fr, c_to)
        roads.append(road)
    # creating a graph instance
    g1 = Graph(cities, roads)
    print("INITIAL")
    print(g1.vtxs)
    print(g1.edges)
    print("")
    print("AFTER UPDATING")
    # Adding a new city (vertex)
    g1.insert_vtx("Kolkata")
    # Adding a new road (edge)
    g1.insert_edge("Delhi", "Kolkata")

    print(g1.vtxs)
    print(g1.edges)
############################################################
############################################################

'''
Graph --> 2 things --> Vertex and Edges

create classes of Vertex and Edge

Vertex class --> name, connected_edges.
Edge class --> startingVertex, EndingVertex, name, weight, directed/un-directed.

create a Graph class

Graph --> list_of_vertices, list_of_edges
          --> Methods => adding a new vertex, adding a new Edge, deleting a vertex/edge, finding path (using different algorithms).
'''
