1. use += instead of s=s1+s2
2. List comprehensions is faster than for loop
3. collections.deque instead of list
4. string.join(iterable) is as  fast as it gets
5.  from sys import stdin
    input = stdin.buffer.readline is much much faster
6  Very efficient trick is to wrap the code of your solution into a function:
    def main():
        # write your solution here

    main()
7. [] is faster than list()
8. {} is faster than dict()
9. set() or {*()} to create empty set
10. sys.maxsize is slower use 10**8 
