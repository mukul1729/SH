class Vector:
    def __init__(self,d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self,j):
        return self._coords[j]
    
    def __setitem__(self,j,val):
        self._coords[j] = val

    def __truediv__(self,other):
        if len(self)!= len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            try:
                result[j] = self[j] / other[j]
            except ZeroDivisionError:
                pass
        return(result)
        
    def __mul__(self,val):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * val
        return result
        
    def __iadd__(self,other):
        for j in range(len(self)):
            a[j] = a[j] + b[j]
        return a
    
    def __eq__(self,other):
        return self._coords == other._coords

    def __ne__(self,other):
        return not self._coords == other._coords

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def pas(self,other):
        return(self._coords)
a = Vector(5)
b = Vector(5)
a[2] = 5
b[2] = 2
print(a*3)
