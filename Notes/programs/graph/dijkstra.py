from heapq import *
class vertex:
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

graph = {1:(vertex(5,1),vertex(2,5),vertex(4,9)),
        2:(vertex(1,5),vertex(3,2)),
        3:(vertex(4,6),vertex(2,2)),
        4:(vertex(1,9),vertex(3,6),vertex(5,2)),
        5:(vertex(4,2),vertex(1,1))}


def dijkstra(graph,n):
    distance = [10000]*(n+1)
    distance[0] = 0
    distance[1] = 0
    q = []
    processed = set()
    heappush(q,(0,1))
    path = {}
    while len(q)!=0:
        a = heappop(q)[1]
        if a in processed:
            continue
        processed.add(a)
        for u in graph[a]:
            b = u.node
            w = u.weight
            if distance[a]+w<distance[b]:
                distance[b] = distance[a]+w
                path[b] = a
                heappush(q,(distance[b],b))
    return distance,path

print(dijkstra(graph,5))
