from collections import deque

def solution(board):
    
    n = len(board)
    m = len(board[0])
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    visited =[ [False] * m for _ in range(n)]
    
    # 시작 위치 찾기
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'R':
                start_r = r
                start_c = c
    
    queue = deque()
    queue.append((start_r, start_c, 0))
    visited[start_r][start_c] = True
    
    while queue:
        r, c, count = queue.popleft()
        
        if board[r][c] == 'G':
            return count
        
        for i in range(4):
            nx = r
            ny = c
            
            while True:
                next_r = nx + dx[i]
                next_c = ny + dy[i]
                
                if not(0 <= next_r < n and 0 <= next_c < m):
                    break
                
                if board[next_r][next_c] == 'D':
                    break
                
                nx = next_r
                ny = next_c
            
            if not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
                
    return -1