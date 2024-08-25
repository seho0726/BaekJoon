A = input().split('-')
ans = 0

for i in A[0].split('+'):
    ans += int(i)

for i in A[1:]:
    for j in i.split('+'):
        ans -= int(j)
        
print(ans)
