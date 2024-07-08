import sys
input = sys.stdin.readline

N = int(input())
X = [0] * 10001

#배열로 선언하여 하나씩 추가
for _ in range(N):
    X[int(input())] += 1

#숫자하나씩 출력
for i in range(len(X)):
    if X[i] != 0:
        for _ in range(X[i]):
            print(i)
