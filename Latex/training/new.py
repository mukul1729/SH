f = {}
def fib(n):
    if n<=1:
        return n
    else:
        if n not in f:
            f[n] = fib(n-1) + fib(n-2)
    return f[n]

print(fib(9))
