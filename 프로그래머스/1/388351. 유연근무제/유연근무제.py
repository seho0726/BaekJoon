def solution(schedules, timelogs, startday):
    
    result = 0

    for i in range (len(schedules)):
        flag = 0
        want_schedules = schedules[i] + 10

        if(want_schedules % 100 >= 60):
            want_schedules = want_schedules + 40
            
        count_start = startday
        for log in timelogs[i]:
            
            if count_start == 6 or count_start == 7:
                count_start += 1
                if count_start > 7:
                    count_start = 1
                continue

            if log > want_schedules:
                flag = 1
                break
        
            count_start += 1
        
        if flag == 0:
            result += 1

    answer = result
    
    return answer