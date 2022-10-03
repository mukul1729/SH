import math
n = 100

prime = [True for i in range(n + 2)]
prime[0] = False
prime[1] = False
 
for i in range(2, n + 2):
    if prime[i]:
        for j in range(i ** 2, n + 2, i):
            prime[j] = False

for a in range(0, n):
    if prime[a] == True:
        print(a,end=',')
