def solution(topping):
    answer = 0
    max_val = 10001 
    
    left_count = [0] * max_val
    right_count = [0] * max_val
    
    left_types = 0
    right_types = 0

    for t in topping:
        if right_count[t] == 0:
            right_types += 1
        right_count[t] += 1
        
    for t in topping:
        # 철수 추가
        if left_count[t] == 0:
            left_types += 1
        left_count[t] += 1
        
        right_count[t] -= 1
        if right_count[t] == 0:
            right_types -= 1
            
        if left_types == right_types:
            answer += 1
            
    return answer