def fibo(n):
    first =0
    second = 1
    for a in range(0,n):
        third=first+second
        first=second
        second=third
    return first
def productFib(prod):
    result = 1
    r=[]
    for a in range(0,2000):
        result=fibo(a)*fibo(a+1)
        if result == prod:
            r.append(fibo(a))
            r.append(fibo(a+1))
            r.append(result==prod)
            break
        elif fibo(a)*fibo(a+1)<prod<fibo(a+1)*fibo(a+2):
            r.append(fibo(a+1))
            r.append(fibo(a+2))
            r.append(result==prod)
            break
    return r
print(productFib(800))
