def solution(elements):
    box = []
    set_box = set(box)
    extend_elements = elements * 2
    
    
    for i in range(len(elements)):
        set_box.add(elements[i])
        
    for i in range(1, len(elements)+1):
        for j in range(len(extend_elements)):
            set_box.add(sum(extend_elements[j:j-1+i]))
    
    
    answer = len(set_box)
    return answer