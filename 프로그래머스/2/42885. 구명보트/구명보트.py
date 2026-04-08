def solution(people, limit):
    
    checklist = sorted(people)
        
    boat = 0
    left = 0
    right = len(checklist) - 1 
    
    while left <= right:
        if checklist[left] + checklist[right] > limit:
            checklist[right] = 0
            right -= 1
            boat += 1
        else:
            checklist[left] = 0
            checklist[right] = 0
            right -= 1
            left += 1
            boat += 1
            
        if left == right:
            boat += 1
            break

        
    answer = boat
    return answer