def solution(k, tangerine):
    table = [0] * 10000001
    
    # 해시 테이블 
    for i in tangerine:
        table[i] += 1
        
    table.sort(reverse=True)
    
    i = 0
    while k > 0:
        k = k - table[i]
        i += 1

    answer = i
    return answer