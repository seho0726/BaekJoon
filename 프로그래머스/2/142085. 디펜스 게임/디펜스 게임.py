import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    pq = []
    
    for i in range(len(enemy)):

        heapq.heappush(pq, enemy[i])
        
        if len(pq) > k:
            last_min = heapq.heappop(pq)
            n -= last_min
            
        if n < 0:
            return i
            
    return len(enemy)