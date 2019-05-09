import networkx as nx
G = nx.Graph()
G.add_node(1)
H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edges_from([(1, 2), (1, 3)])
nx.draw(G, with_labels=True, font_weight='bold')

FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
