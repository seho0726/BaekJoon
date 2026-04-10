def solution(data, ext, val_ext, sort_by):
    data_type = ["code", "date", "maximum", "remain"]
    i = data_type.index(ext)
    s = data_type.index(sort_by)
    
    result=[]
    for x in range(len(data)):
        if data[x][i] < val_ext:
            result.append(data[x])
            
    result.sort(key= lambda x : x[s])
    
    answer = result
    return answer