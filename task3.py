import networkx as nx
import heapq

def getGraph():
    # Створення графа
    G = nx.Graph()

    # Груба транспортна схема м. Бровари
    G.add_edge('A', 'B', weight=2)
    G.add_edge('A', 'C', weight=15)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('B', 'E', weight=2)
    G.add_edge('C', 'G', weight=4)
    G.add_edge('C', 'L', weight=10)
    G.add_edge('D', 'G', weight=2)
    G.add_edge('D', 'K', weight=1)
    G.add_edge('E', 'F', weight=1)
    G.add_edge('E', 'I', weight=1)
    G.add_edge('F', 'D', weight=1)
    G.add_edge('F', 'J', weight=1)
    G.add_edge('G', 'L', weight=7)
    G.add_edge('I', 'J', weight=1)
    G.add_edge('I', 'M', weight=5)
    G.add_edge('J', 'K', weight=1)
    G.add_edge('L', 'M', weight=5)

    return G

def heap_dejkstra(graph : nx.Graph, start: str) -> dict[str, float]:
    '''Search shortes path from start to all other vertexes using heap'''
    dsts = {vertex: -1 for vertex in graph}
    dsts[start] = 0
    pqueue = [(0, start)]

    while pqueue:
        curr_dist, curr_vertex = heapq.heappop(pqueue)
        if curr_dist > dsts[curr_vertex]:
            continue

        for nvertex, params in graph[curr_vertex].items():
            dist = curr_dist + params['weight']
            if dsts[nvertex] == -1 or dist < dsts[nvertex]:
                dsts[nvertex] = dist
                heapq.heappush(pqueue, (dist, nvertex))

    return dsts

def my_dejkstra(graph, start):
    '''Search shortes path from start to all other vertexes'''
    dsts = {vertex: -1 for vertex in graph}
    dsts[start] = 0
    unvisited = list(dsts.keys())

    while unvisited:
        curr = min(unvisited, key=lambda vertex: dsts[vertex] if dsts[vertex] >= 0 else float('infinity'))
        if dsts[curr] == -1:
            break;
        for nvert, prm in graph[curr].items():
            dst = dsts[curr] + prm['weight']
            if dsts[nvert] == -1 or dst < dsts[nvert]:
                dsts[nvert] = dst
        unvisited.remove(curr)

    return dsts

if __name__ == "__main__":
    graph = getGraph()
    
    print("Shortes paths from vertex 'A':")
    print(heap_dejkstra(graph, 'A'))
    # print(my_dejkstra(graph, 'A'))
