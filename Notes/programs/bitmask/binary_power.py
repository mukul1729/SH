# recursive
def mul(a,b):
    if b == 0:
        return 1
    else:
        if b%2 == 0:
            return pow(mul(a,b//2),2) #mul(a,b//2)*mul(a,b//2) is wrong!!
            # or 
            # return mul(a*a,b//2)
        else:
            return a*mul(a,b-1)

print(mul(3,3))

# iterative
def multiply(a,b):
    res = 1
    while b!=0:
        if b%2 == 1:
            res*=a
        a*=a
        b//=2
    return res
print(multiply(3,3))
