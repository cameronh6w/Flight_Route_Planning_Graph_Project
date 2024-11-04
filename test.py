#test
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3,4,5,6,7])

G.add_edge(1,2)
G.add_edges_from([(1,3),(2,4),(2,5),(4,6),(1,7)])

nx.draw_networkx(G, with_labels=True)
plt.savefig("testing.png")
