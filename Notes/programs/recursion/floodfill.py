def flood(scr,row,col,color,replace):
    if row<0 or col<0 or row>=len(scr) or col>=len(scr[0]):
        return
    if scr[row][col] == color:
        scr[row][col] = replace
        flood(scr,row-1,col,color,replace)
        flood(scr,row,col-1,color,replace)
        flood(scr,row,col+1,color,replace)
        flood(scr,row+1,col,color,replace)

scr = [[0,0,0,0],
    [1,1,1,1],
    [0,1,1,0],
    [0,0,1,1],
    [0,0,0,0]]

row = 3
col = 2
print(flood(scr,row,col,1,'P'))
print(scr)
