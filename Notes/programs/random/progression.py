class Progression:

    def __init__(self,start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current == None:
            raise StopIteration()

        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self,start=0,increment=1):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment 

class GeometricProgression(Progression):
    def __init__(self,start=1,d=1):
        super().__init__(start)
        self._d = d

    def _advance(self):
        self._current  *= self._d

class fibonacci(Progression):
    def __init__(self,f ,s):
        super().__init__(f)
        self._s = s
        self._f = f

    def _advance(self):
        self._current = self._f + self._s
        self._f = self._s
        self._s = self._current


a = fibonacci(1,4)
print(a.print_progression(10))
