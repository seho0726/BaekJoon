def solution(schedules, timelogs, startday):
    
    hope_schedules = []
    count = 0
    
    for h in schedules:
        if (int(h) + 10) % 100 >= 60 :
            hope_schedules.append((int(h) // 100 + 1) * 100 + int(h) % 10)
            continue
        hope_schedules.append(int(h) + 10)
        
    for i in range(len(hope_schedules)):
        t = startday
        count += 1
        for x in range(7):
            
            if timelogs[i][x] > hope_schedules[i] and not t >= 6:
                count -= 1
                break
                
            t += 1
            
            if t == 8:
                t = 1
                
    if count < 0:
        count = 0
        
    return count