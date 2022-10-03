from collections import deque

#method 1
def permute(u,s,k):
    for i in range(len(u)):
        e = u.popleft()
        s.append(e)
        if k == 1:
            print(s)
        else:
            permute(u,s,k-1)
        u.append(e)
        s.pop()
u = deque(['a','b','c'])
print(permute(u,[],3))

#method 2
def per(s,pre):
    if len(s) == 0:
        print(pre)
    else:
        for i in range(len(s)):
            rem = s[0:i]+s[i+1:]
            per(rem,pre+s[i])
print(per('abc',''))

