# 미로 탐색은 최단거리이기 때문에 BFS를 사용
# deque을 이용해 queue 자료구조의 동작을 구현한다.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip()))) 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft() # 큐의 동작

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))