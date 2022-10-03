
def towerofhanoi(n,origin,destination,buffer):
    if n<=0:
        return
    towerofhanoi(n-1,origin,buffer,destination)
    print(str(origin)+'->'+str(destination))
    towerofhanoi(n-1,buffer,destination,origin)

print(towerofhanoi(2,1,3,2))
