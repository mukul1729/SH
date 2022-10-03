
import sys
ans = sys.maxsize
N = 4
for bit in range(2 ** (N - 1)):
    for j in range(N):
        if j<N:
            print(j,end='')
        if bit >> j & 1:
            print('\t',j,end='')
    print()


