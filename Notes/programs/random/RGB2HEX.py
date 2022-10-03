def rgb(r,g,b):
    p =[r,g,b]
    result=""
    for char in p: 
        if char>255:
            char=255
        if char<0:
            char=0
        d = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        first = char//16
        second = char%16
        if first>=10:
            first = d[first]
        result+=str(first)
        if second>=10:
            second = d[second]
        result+=str(second)
    return result
print(rgb(254,255,255))
