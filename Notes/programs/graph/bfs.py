from collections import deque

graph = {'A':('B','C','Z'),'B':('D','E'),'D':(),'E':'C','C':(),'Z':()}
start = 'A'

def bfs(graph,start):
    visit = set()
    p = deque([])
    p.append(start)
    while len(p)!=0:
        x = p.popleft()
        print(x)
        for i in graph[x]:
            if i not in visit:
                visit.add(i)
                p.append(i)

print(bfs(graph,start))
