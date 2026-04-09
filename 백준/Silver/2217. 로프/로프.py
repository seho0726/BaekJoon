import sys
input = sys.stdin.readline

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))
    
rope.sort(reverse=True)

ans = 0
for i in range(n):
    current_weight = rope[i] * (i + 1)
    
    if current_weight > ans:
        ans = current_weight

print(ans)