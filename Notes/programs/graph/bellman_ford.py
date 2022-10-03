edge = []
v,e = map(int,input().split())
for i in range(e):
    a,b,w = map(int,input().split())
    edge.append([a,b,w])
distance = [10000]*(v)
distance[0] = 0
distance[1] = 0
for i in range(0,v-1):
    for e in edge:
        a,b,w = e
        distance[b] = min(distance[b],distance[a]+w)
print(distance)

#input
'''
6 7
1 3 3
1 4 7
1 2 5
2 4 3
2 5 2
3 4 1
4 5 2
'''
