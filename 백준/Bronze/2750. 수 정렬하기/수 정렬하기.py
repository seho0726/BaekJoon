#입력
N = int(input())
X = []

#배열로 선언하여 하나씩 추가
for i in range(1, N+1):
    X.append(int(input()))

#오름차순 정렬
X.sort()

#숫자하나씩 출력
for p in range(N):
    print(X[p])
