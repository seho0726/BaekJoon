import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    
    #DP에 대해서 찾아서 풀이한 부분
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])
    
#다이나믹 프로그래밍이란 앞에서 계산한식을 배열에 미리 저장하여 연산속도를 증가시키는 프로그래밍을 의미함
