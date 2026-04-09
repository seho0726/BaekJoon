from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    answer = []
    visited = [[False] * m for _ in range(n)]
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def bfs(r, c):
        q = deque([(r, c)])
        visited[r][c] = True
        total = int(maps[r][c])
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        total += int(maps[nx][ny])
                        q.append((nx, ny))
        return total
    
    for a in range(n):
        for b in range(m):
            if maps[a][b] != 'X' and not visited[a][b]:
                answer.append(bfs(a, b))
                
    if not answer:
        return [-1]
    
    return sorted(answer)