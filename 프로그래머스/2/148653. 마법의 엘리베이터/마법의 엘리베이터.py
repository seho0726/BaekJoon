def solution(storey):
    count = 0
    
    while storey > 0:
        a1 = storey % 10        
        a2 = (storey // 10) % 10 
        
        if a1 > 5:
            
            count += (10 - a1)
            storey += (10 - a1) 
        elif a1 < 5:
            count += a1
        else:
            if a2 >= 5:
                count += 5
                storey += 5
            else:
                count += 5
        
        storey //= 10
                
    return count