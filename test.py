#test
import matplotlib.pyplot as plt
import networkx as nx

#create vertices and edges
G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3,4,5,6,7])

G.add_edges_from([(1,2),(1,3),(2,4),(2,5),(4,6),(1,7)])

#add weighted edges (cost of flight)
edges = [
    (1,2,500),
    (1,3,300),
    (2,4,400),
    (2,5,100),
    (4,6,450),
    (1,7,600)
]

G.add_weighted_edges_from(edges)

#find shortest path
start_airport = 7
end_airport = 6

shortest_path = nx.dijkstra_path(G, start_airport, end_airport)
shortest_distance = nx.shortest_path_length(G, start_airport, end_airport)

#draw graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True)

path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist = path_edges, edge_color = "red")

edge_labels = {(u, v): f"{d['weight']} km" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="blue")

print("Shortest path from node", start_airport, "to node", end_airport, ":")
for i in range(len(shortest_path) - 1):
    u = shortest_path[i]
    v = shortest_path[i + 1]
    weight = G[u][v]['weight']
    print(f"Node {u} to Node {v}, Weight: {weight} km")


plt.savefig("weighted1.png")
plt.show()


