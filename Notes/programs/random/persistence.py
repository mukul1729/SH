'''Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in num until you reach a single digit.'''
def persistence(n):
    num=1
    count=1
    if n<10:
        return 0
    while True:
        if n==0:
            count+=1
            n=num
            num=1
        mod = n % 10
        n = n // 10
        num = num* mod
        if n==0 and num<10:
            break
    return count
