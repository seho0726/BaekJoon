import sys
sys.setrecursionlimit(10000)

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    answer = []
    
    visited = [[False] * m for _ in range(n)]
                
    def dfs(x, y):
        
        if y < 0 or y >= m or x < 0 or x >= n or visited[x][y] or maps[x][y] == 'X':
            return 0
        
        visited[x][y] = True

        total = int(maps[x][y])
        total += dfs(x+1, y)
        total += dfs(x-1, y)
        total += dfs(x, y+1)
        total += dfs(x, y-1)
        return total
        
        
    for a in range(n):
        for b in range(m):
            if maps[a][b] != 'X' and not visited[a][b]:
                res = dfs(a, b)
                if res > 0:
                    answer.append(res)

    if not answer:
        return [-1]
    return sorted(answer)