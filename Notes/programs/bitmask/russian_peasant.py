# recursive
def add(a,b):
    if b == 0:
        return 0
    else:
        if b%2 == 0:
            return 2*(add(a,b//2)) #mul(a,b//2)+mul(a,b//2) is wrong!!
            # or return (add(a+a,b//2)) 
        else:
            return a+add(a,b-1)

print(add(3,3))

# iterative
def addition(a,b):
    res = 0
    while b!=0:
        if b%2 == 1:
            res+=a
        a+=a
        b//=2
    return res
print(addition(3,3))
