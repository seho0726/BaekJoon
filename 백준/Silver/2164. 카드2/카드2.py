N = int(input())
n = 0

if N == 1:
    print(N)
if N > 1:
    while 2 ** n < N:
        n = n + 1
    ans = (N - 2 ** (n - 1)) * 2
    print(ans)
