class queen:
    def __init__(self):
        self.x = [[0 for i in range(8)] for j in range(8)]

    def getqueen(self,i,j,deltax,deltay):
        r = i+deltay
        c = j+deltax
        k = 0
        while r>=0 and r<8 and c>=0 and c<8:
            k+=self.x[r][c]
            r+=deltay
            c+=deltax
        return k

    def solve(self,col):
        if col == 8:
            print(self.printboard())
            return
        for i in range(8):
            nqueen = self.getqueen(i,col,-1,0)
            nqueen += self.getqueen(i,col,1,0)
            nqueen += self.getqueen(i,col,-1,-1)
            nqueen += self.getqueen(i,col,1,-1)
            nqueen += self.getqueen(i,col,-1,1)
            nqueen += self.getqueen(i,col,1,1)
            if nqueen == 0:
                self.x[i][col] = 1
                self.solve(col+1)
                self.x[i][col] = 0

    def printboard(self):
        for i in self.x:
            print(i)


a = queen()
print(a.solve(0))
