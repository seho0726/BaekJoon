# 각 필요한 값을 입력 받는다.
N, X = map(int,input().split())
A = list(map(int, input().split()))

while len(A) > N:
    A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=' ')


