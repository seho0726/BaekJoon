def solution(bandage, health, attacks):
    time = 0
    answer = 0
    attack = len(attacks)
    max_health = health
    success_time = 0
    
    while True:
        flag = 0
        time += 1
        
        if attack <= 0:
            answer = health
            break   

        for x, y in attacks:
            if time == x:
                health -= y
                success_time = 0
                attack -= 1
                flag = 1
                
        if health <= 0:
            answer = -1
            break            
                    
        if flag == 1:
            continue
            
        health = health + bandage[1]
        success_time += 1
        if health >= max_health:
            health = max_health                
                
        if success_time == bandage[0]:
            health += bandage[2]
            success_time = 0
            if health >= max_health:
                health = max_health
            

    
    return answer