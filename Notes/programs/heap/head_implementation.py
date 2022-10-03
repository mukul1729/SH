class base:
    class item:
        def __init__(self,data,value):
            self.key = data
            self.value = value
        def __lt__(self,other):
            return self.key<other.key

class heap(base):
    def is_empty(self):
        return len(self.data) == 0
    def parent(self,j):
        return (j-1)//2
    def left(self,j):
        return 2*j+1
    def right(self,j):
        return 2*j+2
    def has_left(self,j):
        return self.left(j)<len(self.data)
    def has_right(self,j):
        return self.right(j)<len(self.data)
    def swap(self,i,j):
        self.data[i],self.data[j] = self.data[j],self.data[i]
    def upheap(self,j):
        parent = self.parent(j)
        if j>0 and self.data[parent]>self.data[j]:
            self.swap(parent,j)
            self.upheap(parent)
    def downheap(self,j):
        if self.has_left(j):
            small = self.left(j)
            if self.has_right(j):
                if self.data[self.right(j)]<self.data[small]:
                    small = self.right(j)
            if self.data[j] > self.data[small]:
                self.swap(j,small)
                self.downheap(small)
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def add(self,key,value):
        self.data.append(self.item(key,value))
        self.upheap(len(self.data)-1)
    def min(self):
        if self.is_empty():
            raise Empty("Its uhhh")
        item = self.data[0]
        return (item.key,item.value)
    def show(self):
        for i in self.data:
            print(i.key,i.value)
    def remove_min(self):
        if self.is_empty():
            raise Empty("UTs fd")
        self.swap(0,len(self.data)-1)
        item = self.data.pop()
        self.downheap(0)
        return item.key,item.value

a = heap()
a.add(9,4)
a.add(1,2)
a.add(2,4)
print(a.remove_min())
print(a.remove_min())
print(a.remove_min())
print(a.show())
