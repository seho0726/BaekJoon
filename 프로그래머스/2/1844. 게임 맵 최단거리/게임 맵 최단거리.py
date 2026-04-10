from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * (m+1) for _ in range(n+1)]
    
    q = deque()
    q.append((0,0,1))
    visited[0][0] = True
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    answer = 0
    while q:
        x, y, dist = q.popleft()
        
        if x == n-1 and y == m-1:
            answer = dist
            break
            
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny < 0 or ny >= m or visited[nx][ny]:
                continue
                
            if maps[nx][ny] == 1:
                q.append((nx, ny, dist+1))
                visited[nx][ny] = True
        
        answer = -1
        
    return answer