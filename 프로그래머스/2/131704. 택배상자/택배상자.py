def solution(order):

    stack = []
    idx = 0
    i = 1
    count = 0
    
    while count < len(order):
        
        if order[idx] == i:
            count += 1
            idx += 1
            i += 1
            
        if order[idx] > i:
            stack.append(i)
            i += 1
            
        if order[idx] < i:
            if order[idx] == stack[-1]:
                stack.pop()
                count += 1
                idx += 1
            else:
                break
                
    return count