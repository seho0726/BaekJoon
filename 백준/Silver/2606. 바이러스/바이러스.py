from collections import deque
import sys

input = sys.stdin.readline

n = int(input())  
v = int(input())  

graph = [[] for _ in range(n + 1)]
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

visited = [0] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        curr = queue.popleft()

        for next_node in graph[curr]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)

bfs(1)

print(sum(visited) - 1)