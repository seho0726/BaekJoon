#2차원 배열로 나타내면 되지 않을까?
arr = [list(map(str,input().split())) for _ in range(20)]
sum = 0
total = 0
def trans(G):
    if G == 'A+':
        return 4.5
    elif G == 'A0':
        return 4.0
    elif G == 'B+':
        return 3.5
    elif G == 'B0':
        return 3.0
    elif G == 'C+':
        return 2.5
    elif G == 'C0':
        return 2.0
    elif G == 'D+':
        return 1.5
    elif G == 'D0':
        return 1.0
    elif G == 'F':
        return 0.0
    else:
        print('error')

for i in arr:
    if i[2] == 'P':
        continue
    sum = sum + float(i[1]) * float(trans(i[2]))
    total = total + float(i[1])

print(round(sum/total, 6))
