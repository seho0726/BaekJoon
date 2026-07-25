from collections import deque

def solution(n, computers):
    
    visited = [False for _ in range(n)]
    answer = 0
    
    def bfs(start, computers):
        nonlocal answer
    
        visited[start] = True
        q = deque([start])

        while q:
            i = q.popleft()

            for x in range(n):
                if x == i:
                    continue

                if computers[i][x] == 1 and visited[x] == False:
                    visited[x] = True
                    q.append(x)
                    
    for x in range(n):
        if visited[x] == False:
            bfs(x, computers)
            answer += 1
    
    return answer