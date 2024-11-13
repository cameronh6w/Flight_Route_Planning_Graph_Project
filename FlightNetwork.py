#test
import matplotlib.pyplot as plt
import networkx as nx

#create vertices and edges
G = nx.DiGraph()

allAirports = ["SEA","LAX","LAS","PHX","ABQ","DEN","WYS","LBF","DFW","MCI","MSP","ORD","DTW","JFK","BOS","PHL","EWR","IND","CLT","MCO","ATL"]

G.add_nodes_from(allAirports)

G.add_edges_from([("SEA","LAX"),
                  ("SEA","LAS"),
                  ("DEN","SEA"),
                  ("WYS","SEA"),
                  ("LAX","PHX"), #
                  ("LAX","LAS"),
                  ("LAX","ABQ"),
                  ("LAS","PHX"),
                  ("LAS","DEN"),
                  ("DEN","MCI"), #
                  ("DEN","LBF"),
                  ("DEN","WYS"),
                  ("PHX","DEN"),
                  ("PHX","ABQ"),
                  ("ABQ","DFW"), #
                  ("ABQ","LAX"),
                  ("WYS","LBF"),
                  ("LBF","MSP"),
                  ("MSP","LBF"),
                  ("MSP","MCI"), #
                  ("MSP","DTW"),
                  ("MCI","DFW"),
                  ("MCI","ATL"),
                  ("MCI","ORD"),
                  ("DFW","DEN"), #
                  ("DFW","MCO"),
                  ("ATL","DFW"),
                  ("ATL","MCO"),
                  ("ATL","ORD"),
                  ("ORD","MSP"), #
                  ("MCO","CLT"),
                  ("MCO","IND"),
                  ("IND","ATL"),
                  ("IND","PHL"),
                  ("IND","CLT"), #
                  ("ORD","IND"), 
                  ("ORD","PHL"),
                  ("ORD","JFK"),
                  ("CLT","EWR"),
                  ("EWR","BOS"), #
                  ("PHL","EWR"), 
                  ("PHL","JFK"),
                  ("BOS","MSP"),
                  ("BOS","DTW"),
                  ("JFK","DTW"), #
                  ("JFK","BOS"), 
                  ("BOS","JFK")])

#add weighted edges (cost of flight)
edges = ([
        ("SEA","LAX",955),
        ("SEA","LAS",866),
        ("DEN","SEA",1022),
        ("WYS","SEA",570),
        ("LAX","PHX",370), #
        ("LAX","LAS",240),
        ("LAS","PHX",260),
        ("LAS","DEN",630),
        ("DEN","MCI",531), #
        ("DEN","LBF",241),
        ("DEN","WYS",1022),
        ("PHX","DEN",600),
        ("PHX","ABQ",330),
        ("ABQ","DFW",570), #
        ("ABQ","LAX",680),
        ("WYS","LBF",570),
        ("LBF","MSP",465),
        ("MSP","LBF",465),
        ("MSP","MCI",390), #
        ("MSP","DTW",850),
        ("MCI","DFW",460),
        ("MCI","ATL",690),
        ("MCI","ORD",400),
        ("DFW","DEN",640), #
        ("DFW","MCO",985),
        ("ATL","DFW",730),
        ("ATL","MCO",400),
        ("ATL","ORD",600),
        ("ORD","MSP",330), #
        ("MCO","CLT",470),
        ("MCO","IND",870),
        ("IND","ATL",465),
        ("IND","PHL",580),
        ("IND","CLT",460), #
        ("ORD","IND",670), 
        ("ORD","PHL",676),
        ("ORD","JFK",740),
        ("CLT","EWR",530),
        ("EWR","BOS",200), #
        ("PHL","EWR",80), 
        ("PHL","JFK",95),
        ("BOS","MSP",1120),
        ("BOS","DTW",1560),
        ("JFK","DTW",1389), #
        ("JFK","BOS",186), 
        ("BOS","JFK",186)
        ])

G.add_weighted_edges_from(edges)

print("AVAILABLE AIRPORTS:")
for item in allAirports:
    print(item)

#find shortest path
start_airport = input("\nChoose your starting airport: ")
end_airport = input("Choose your ending airport: ")

shortest_path = nx.dijkstra_path(G, start_airport, end_airport)
shortest_distance = nx.dijkstra_path_length(G, start_airport, end_airport)

# Define colors for nodes
node_colors = []
for node in G.nodes():
    if node == start_airport:
        node_colors.append("green")  # Starting node color
    elif node == end_airport:
        node_colors.append("red")  # Ending node color
    else:
        node_colors.append("yellow")  # Default color for other nodes

#draw graph
pos = nx.spring_layout(G, k = 20, weight='weight', scale = 4, iterations = 50)
nx.draw_networkx(G, pos, node_color=node_colors, with_labels=True, node_size=500, font_size=8)

path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist = path_edges, edge_color = "red",width = 2)

# edge_labels = {(u, v): f"{d['weight']} miles" for u, v, d in G.edges(data=True)}
edge_labels = {(u, v): f"{d.get('weight', 'N/A')} miles" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size = 5, font_color="blue")

print("Shortest path from node", start_airport, "to node", end_airport, ":")
for i in range(len(shortest_path) - 1):
    u = shortest_path[i]
    v = shortest_path[i + 1]
    weight = G[u][v]['weight']
    print(f"Node {u} to Node {v}, Weight: {weight} miles")

print(f"\nTotal distance from {start_airport} to {end_airport}: {shortest_distance} miles")

plt.savefig("flightNetworkGraph.png")
plt.show()


