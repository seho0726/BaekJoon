from itertools import combinations
def solution(weights):
    loc = [2, 3, 4]
    table = [0] * 100002
    count = 0
    
    for i in weights:
        table[i] += 1
    
    # 같은 것을 뽑는 경우
    for t in table:
        if t >= 2:
            count += t * (t-1) // 2
    
    weights_set = set(weights)
    weights_com_list = combinations(weights_set, 2)
    
    for a, b in weights_com_list:
        if a == b:
            continue
        for x in loc:
            for y in loc:
                if a * x == b * y:
                    count += table[a] * table[b]
        
    answer = count
    return answer