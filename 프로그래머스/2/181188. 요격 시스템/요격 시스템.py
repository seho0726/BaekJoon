def solution(targets):
    
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_shot = -1.0
    
    for s, e in targets:

        if s >= last_shot:
            answer += 1 
            last_shot = e 
            
    return answer