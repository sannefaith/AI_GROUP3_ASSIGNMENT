import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","STC","J1","Phase3","ParkingLot","Mada"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge
G.add_edge("SportsComplex","Siwaka", weight="450",)
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase2","STC",weight="50")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("Mada","ParkingLot",weight="700")

# #position the nodes to resemble Nairobis map
G.nodes( data='name',default=None)
G.nodes["SportsComplex"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(4,0)
G.nodes["Ph.1A"]['pos']=(8,0)
G.nodes["Ph.1B"]['pos']=(8,-4)
G.nodes["Phase2"]['pos']=(12,-4)
G.nodes["STC"]['pos']=(8,-8)
G.nodes["J1"]['pos']=(16,-4)
G.nodes["Phase3"]['pos']=(16,-8)
G.nodes["ParkingLot"]['pos']=(16,-12)
G.nodes["Mada"]['pos']=(20,-4)


node_pos = nx.get_node_attributes(G,'pos')
edge_col = ['black']
node_col = ['darkturquoise']

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=1500)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('on')
plt.show()

graph = {
'Strathmore Sports Complex':[('Siwaka Plaza',405)],
'Siwaka Plaza':[('Ph.1A',380), ('Ph.1B',280)],
'Ph.1A':[('Mada',630), ('Siwaka Plaza',405),('Ph.1B',280)],
'Ph.1B':[('Siwaka Plaza',405),('Ph.1A',380), ('STC',213),('Phase 2',210)],
'Mada':[('Ph.1A',380),('Parking Lot',0)],
'STC':[('Ph.1B',280),('Phase 2',210), ('Parking Lot',0)],
'Phase 2':[('J1',500),('Ph.1B',280),('STC',213),('Phase 3',160)],
'Phase 3':[('Phase 2',210),('Parking Lot',0)],
'J1':[(('Mada',630),('Phase 2',210))],
'Mada':[(('J1',500),('Parking Lot',0))]
}

def bfs(start, target, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)
    queue=queue+[x for x in graph[start] if x[0][0] not in visited]
    queue.sort(key=lambda x:x[1])
    if queue[0][0]==target:
        print(queue[0][0])
    else:
        processing=queue[0]
        queue.remove(processing)
        bfs(processing[0], target, graph, queue, visited)
bfs('Strathmore Sports Complex', 'Parking Lot', graph)