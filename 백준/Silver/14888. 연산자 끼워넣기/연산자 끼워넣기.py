N = int(input())
A = list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)


def cal(x, y):
    global add, sub, mul, div, max_value, min_value
    if x == N:
        max_value = max(max_value, y)
        min_value = min(min_value, y)
        return 
    else:
        if add > 0:
            add = add - 1
            cal(x+1, y + A[x])
            add = add + 1
        if sub > 0:
            sub = sub - 1
            cal(x+1, y - A[x])
            sub = sub + 1
        if mul > 0:
            mul = mul - 1
            cal(x+1, y * A[x])
            mul = mul + 1
        if div > 0:
            div = div - 1
            cal(x+1, int(y / A[x]))
            div = div + 1

cal(1, A[0])

print(max_value)
print(min_value)
