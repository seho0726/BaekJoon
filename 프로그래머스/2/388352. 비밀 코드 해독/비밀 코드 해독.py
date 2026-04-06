from itertools import combinations

def solution(n, q, ans):
    result = 0
    
    set_q = [set(query) for query in q]
    m = len(q) # 시도 횟수
    
    numbers = list(range(1, n + 1))
    
    for trial in combinations(numbers, 5):
        flag = True
        trial_set = set(trial) 

        for i in range(m):
            if len(trial_set & set_q[i]) != ans[i]:
                flag = False
                break
        
        if flag:
            result += 1
            
    return result