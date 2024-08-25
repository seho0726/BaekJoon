import sys

N, K = map(int, sys.stdin.readline().split())
A = []

for i in range(N):
    A.append(int(sys.stdin.readline()))
count = 0

A.sort(reverse=True)

for i in A:
    if K >= i:
        count = count + (K // i)
        K = K % i
        if K <= 0:
            break
print(count)
        
