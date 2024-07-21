# 배열을 다 0으로 선언하고 거리 겹치는 부분을 1로 선언하는것은 메모리와 시간에 대한 문제가 발생
# 우선순위, 힙을 사용

import sys
import heapq

n = int(sys.stdin.readline().strip())
locations = []
for _ in range(n):
    h, o = map(int, sys.stdin.readline().strip().split())
    locations.append((min(h, o), max(h, o)))

locations.sort(key=lambda x: (x[1],x[0]))

d = int(input())
heap = []
max_cnt = 0
for location in locations:
    start, end = location
    heapq.heappush(heap, start)
    line_start = end - d
    while heap and heap[0] < line_start:
        heapq.heappop(heap)
    max_cnt = max(max_cnt, len(heap))

print(max_cnt)

