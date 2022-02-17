
class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def __repr__(self) -> str:
        return self.name


v1 = Vertex("D")
v2 = Vertex("M")
v3 = Vertex("B")


class Edge:
    def __init__(self,  vtx_from, vtx_to, weight=None):
        self.weight = weight
        self.vtx_from = vtx_from
        self.vtx_to = vtx_to


class Graph:
    def __init__(self, list_of_vtxs=[], list_of_edges=[]):
        self.vtxs = list_of_vtxs
        self.edges = list_of_edges

    def add_vertex(self, new_vtx_name):
        new_vtx = Vertex(new_vtx_name)
        self.vtxs.append(new_vtx)


if __name__ == "__main__":

    vtx_list = ["D", "M", "B", "P"]
    vertexes = []
    for v in vtx_list:
        v_obj = Vertex(v)
        vertexes.append(v_obj)

    edges_list = [('M', 'B'), ('M', 'P'), ('P', 'B'),
                  ('B', 'M'), ('P', 'M'), ('B', 'P')]

    g1 = Graph(list_of_vtxs=vertexes, list_of_edges=edges_list)
    print(g1.vtxs)
    g1.add_vertex('K')
    print(g1.vtxs)
    print(g1.edges)
