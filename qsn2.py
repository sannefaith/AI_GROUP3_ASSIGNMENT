

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
        
bfs('Strathmore Sports Complex', 'Parking Lot',graph)