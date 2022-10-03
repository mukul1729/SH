from collections import deque

graph = {'A':('B','C','Z'),'B':('D','E'),'D':(),'E':'C','C':(),'Z':()}
start = 'A'

def dfs(graph,start):
    visit = set()
    visit.add(start)
    q = deque([])
    q.append(start) #stack is used in dfs
    while len(q)!=0:
        x = q.popleft()
        print(x)
        for i in graph[x]:
            if i not in visit:
                visit.add(i)
                q.append(i)

print(dfs(graph,start))
