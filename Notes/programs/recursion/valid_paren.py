def valid(n):
    if n == 1:
        return ['()']
    else:
        prev = valid(n-1)
        ans = []
        for i in prev:
            first = i
            for i in range(len(first)):
                p = first[0:i]+'()'+first[i:]
                ans.append(p)
        return list(set(ans))
print(valid(3))


l = []
def valid(left,right,s,c):
    global l
    if left<0 or right<left:
        return
    if left == 0 and right == 0:
        l.append(''.join(s))
    else:
        if left>0:
            s[c] = '('
            valid(left-1,right,s,c+1)
        if right>left:
            s[c] = ')'
            valid(left,right-1,s,c+1)


c = 3
s = ['']*(2*c)
(valid(c,c,s,0))
print(l)
