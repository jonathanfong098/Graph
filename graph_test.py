from graph import Graph


def test_graph():
    """
    This function tests to see if the graph works.
    """
    graph = Graph()
    graph.add_vertex('A')
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 1)
    graph.add_vertex('B')
    graph.add_edge('B', 'E', 4)
    graph.add_vertex('C')
    graph.add_edge('C', 'B', 2)
    graph.add_edge('C', 'D', 4)
    graph.add_vertex('E')

    vertices = graph.vertices
    print('Adjacency list for graph:', vertices)
    print()

    edges = graph.all_edges()
    print('Vertex:{Neighbor Vertex:weight of connection} = ', edges)


if __name__ == '__main__':
    test_graph()

"""test_graph output 
/Users/jonathanfong/PycharmProjects/graph/venv/bin/python /Users/jonathanfong/PycharmProjects/graph/graph_test.py
Adjacency list for graph: {'A': <vertex.Vertex object at 0x100d5ba30>, 'B': <vertex.Vertex object at 0x100e01070>, 'C': <vertex.Vertex object at 0x100e019a0>, 'E': <vertex.Vertex object at 0x100e01c10>, 'D': <vertex.Vertex object at 0x100e01ac0>}

Vertex:{Neighbor Vertex:weight of connection} =  {'A': {'C': 1, 'B': 4}, 'B': {'E': 4}, 'C': {'D': 4, 'B': 2}, 'E': {}, 'D': {}}

Process finished with exit code 0
"""