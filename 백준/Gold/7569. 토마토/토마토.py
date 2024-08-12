import sys
from collections import deque

#이런 방식으로 input을 쉽게 정의하는 방식을 사용하더라.
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()

# 탐색
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue

            if box[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))


bfs()

tomato_max = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            tomato_max = max(tomato_max, box[i][j][k])

print(tomato_max - 1)