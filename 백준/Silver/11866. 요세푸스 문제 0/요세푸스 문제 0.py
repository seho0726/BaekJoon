
# 덱을 사용하는 방법
# 덱에서 옆에서 있는것을 떼어다가 오른쪽으로 붙혀주는 작업을 K-1만큼 시도한다.
# 그리고나서 K번째의 결과를 다른 결과에 붙혀넣는다.
import sys
from collections import deque

queue = deque()
result = []

N, K = map(int, sys.stdin.readline().split())

for i in range(1, N + 1):
    queue.append(i)

while queue:
    for i in range(K - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")