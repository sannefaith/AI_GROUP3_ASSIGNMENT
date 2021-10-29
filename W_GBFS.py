import networkx as nx
import matplotlib.pyplot as plt
import queue as Q
from collections import defaultdict
def gbfs(adjacencyList, heuristics):
    i = 0
    sVertex=max(heuristics,key=heuristics.get)
    print(sVertex)
    fVertex=min(heuristics,key=heuristics.get)
    print(fVertex)
    visitedSet = set()
    queue = []
    visitedSet.add(sVertex)
    queue.append(sVertex)
    result=[]
    while queue:
        search=[]
        v = queue[i]
        if v == fVertex:
            result.append(v)
            break
        result.append(v)
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                search.append(heuristics[neighbor])
        x = min(search,default="Nimededi")
        for k, v in heuristics.items():
            if x == v:
                queue.append(k)
                visitedSet.add(k)
        i+=1
    return result
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList
edges = [["SportsComplex","Siwaka"]
         ,["Siwaka","Ph1.A"]
         ,["Ph1.A","Ph1.B"]
         ,["Siwaka","Ph1.B"]
         ,["Ph1.A","Mada"]
         ,["Ph1.B","Phase2"]
         ,["Ph1.B","STC"]
         ,["STC","Phase2"]
         ,["STC","ParkingLot"]
         ,["Phase2","J1"]
         ,["Phase2","Phase3"]
         ,["Phase3","ParkingLot"]
         ,["J1","Mada"]
         ,["Mada","ParkingLot"]]
adjacencyList = generateAdjacencyLst(edges)
heuristics = {
    'SportsComplex':730,
    'Siwaka':405,
    'Ph1.A':380,
    'Ph1.B':280,
    'STC':213,
    'Phase2':210,
    'J1':500,
    'Phase3':160,
    'Mada':630,
    'ParkingLot':0
    }
print(gbfs(adjacencyList,heuristics))
