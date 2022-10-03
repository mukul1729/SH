def find_outlier(integers):
    e = 0
    o = 0
    for a in range(0,3):
        if integers[a]%2 == 0:
            e = e + 1 
    if e>=2:
        for a in integers:
            if a%2 != 0:
                return(a)
                exit()
    else:
        for a in integers:
            if a%2 == 0:
                return(a)
                exit()

print(find_outlier([3,5,4,7,9]))
