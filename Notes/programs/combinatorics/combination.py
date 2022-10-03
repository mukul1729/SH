# iterative
a = [1,2,3]
limit = 1<<len(a)
for i in range(limit):
    for j in range(len(a)):
        if (i>>j)&1:
            print(a[j],end='')
    print()


# recursive
def search(s,k):
    if k == 3:
        print(s)
    else:
        search(s,k+1)
        s.append(k)
        search(s,k+1)
        s.pop()
