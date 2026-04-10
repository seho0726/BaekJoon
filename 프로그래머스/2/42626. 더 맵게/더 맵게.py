import heapq
def solution(scoville, K):
    
    count = 0
    q = []
    for i in range(len(scoville)):
        heapq.heappush(q, scoville[i])
    
    while q :
        a = heapq.heappop(q)
        if a >= K :
            heapq.heappush(q, a)
            break
        elif a < K and q:
            b = heapq.heappop(q)
            c = a + (b * 2)
            heapq.heappush(q, c)
            count += 1
        else:
            count = -1

    answer = count
    return answer