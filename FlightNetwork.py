import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches  # For custom legend patches


#create a directional graph
G = nx.DiGraph()

# list of all nodes in the graph
all_airports = ["SEA","LAX","LAS","PHX","ABQ","DEN","WYS","LBF","DFW","MCI","MSP","ORD","DTW","JFK","BOS","PHL","IND","CLT","MCO","ATL"]

# create a dictionary mapping airport code names to full names (used when printing to user)
# Dictionary mapping airport codes to full names
airport_full_names = {
    "SEA": "Seattle-Tacoma International Airport",
    "LAX": "Los Angeles International Airport",
    "LAS": "Harry Reid International Airport (Las Vegas)",
    "PHX": "Phoenix Sky Harbor International Airport",
    "ABQ": "Albuquerque International Sunport",
    "DEN": "Denver International Airport",
    "WYS": "West Yellowstone Airport",
    "LBF": "North Platte Regional Airport",
    "DFW": "Dallas/Fort Worth International Airport",
    "MCI": "Kansas City International Airport",
    "MSP": "Minneapolis-Saint Paul International Airport",
    "ORD": "Chicago O'Hare International Airport",
    "DTW": "Detroit Metropolitan Wayne County Airport",
    "JFK": "John F. Kennedy International Airport",
    "BOS": "Boston Logan International Airport",
    "PHL": "Philadelphia International Airport",
    "IND": "Indianapolis International Airport",
    "CLT": "Charlotte Douglas International Airport",
    "MCO": "Orlando International Airport",
    "ATL": "Hartsfield-Jackson Atlanta International Airport"
    }

# add the nodes to the graph
G.add_nodes_from(all_airports)


# create list of edges between airports + weights to the edges (distance between airports)
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
        ("DEN","WYS",470),
        ("PHX","DEN",600),
        ("PHX","ABQ",330),
        ("ABQ","DFW",570), #
        ("ABQ","LAX",680),
        ("WYS","LBF",580),
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
        ("PHL","JFK",95),
        ("BOS","MSP",1125),
        ("BOS","DTW",630),
        ("JFK","DTW",509), #
        ("JFK","BOS",187), 
        ("BOS","JFK",187)
        ])

# add the edges to the graph
G.add_weighted_edges_from(edges)

# add coordinates to the edges based on the location on a map
positions = {
    "SEA": (-122, 47), "LAX": (-118, 34), "LAS": (-115, 38), "PHX": (-112, 31), "ABQ": (-106, 35),
    "DEN": (-104, 39), "WYS": (-111, 44), "LBF": (-100, 42), "DFW": (-97, 32), "MCI": (-94, 39),
    "MSP": (-93, 45), "ORD": (-87, 41), "DTW": (-83, 42), "JFK": (-70, 41), "BOS": (-68, 45),
    "PHL": (-75, 39), "IND": (-90, 38), "CLT": (-78, 36), "MCO": (-81, 28),
    "ATL": (-83, 33)
}

# print list of available airports to the user
print("AVAILABLE AIRPORTS:")
for code_name, full_name in airport_full_names.items():
    print(f"{code_name}: {full_name}")

# get user input for starting and ending nodes
while True:
    try:
        start_airport = input("\nChoose your starting airport (enter code): ")
        if start_airport not in all_airports:
            raise ValueError("Invalid starting airport code.")
        
        end_airport = input("Choose your ending airport (enter code): ")
        if end_airport not in all_airports:
            raise ValueError("Invalid ending airport code.")
        
        break

    except ValueError as e:
        print(f"Error: {e} Please pick a valid airport code from the list above.")

#find shortest path using dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, start_airport, end_airport)

# calculate shortest distance using dijkstra's algorithm
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
nx.draw_networkx(G, pos=positions, node_color=node_colors, with_labels=True, node_size=500, font_size=8)

path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos = positions, edgelist = path_edges, edge_color = "red",width = 2)

# edge_labels = {(u, v): f"{d['weight']} miles" for u, v, d in G.edges(data=True)}
edge_labels = {(u, v): f"{d.get('weight', 'N/A')} miles" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos = positions, edge_labels=edge_labels, font_size = 5, font_color="blue")

# Add legend
start_patch = mpatches.Patch(color="green", label="Start Airport")
end_patch = mpatches.Patch(color="red", label="End Airport")
other_patch = mpatches.Patch(color="yellow", label="Other Airports")
plt.legend(handles=[start_patch, end_patch, other_patch], loc="lower right")

print("Shortest path from node", start_airport, "to node", end_airport, ":")
for i in range(len(shortest_path) - 1):
    u = shortest_path[i]
    v = shortest_path[i + 1]
    weight = G[u][v]['weight']
    print(f"Node {u} to Node {v}, Weight: {weight} miles")

print(f"\nTotal distance from {start_airport} to {end_airport}: {shortest_distance} miles")

plt.savefig("flightNetworkGraph.png")
plt.show()


