from collections import deque

def solution(x, y, n):
    if x == y:
        return 0

    visited = set()
    visited.add(x)

    queue = deque([(x, 0)])
    
    while queue:
        curr, count = queue.popleft()
        
        for next_val in (curr + n, curr * 2, curr * 3):
            
            if next_val == y:
                return count + 1
            
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, count + 1))
                
    return -1