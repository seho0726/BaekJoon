def solution(picks, minerals):
    total_picks = sum(picks)
    minerals = minerals[:total_picks * 5]
    
    groups = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5]
        groups.append([chunk.count("diamond"), chunk.count("iron"), chunk.count("stone")])
    
    groups.sort(key= lambda x : (-x[0], -x[1], -x[2]))
    answer = 0
    for g in groups:
        dia, iron, stone = g
            
        if picks[0] > 0:
            answer += (dia + iron + stone)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += (dia*5 + iron + stone)
            picks[1] -= 1
        elif picks[2] > 0:
            answer += (dia*25 + iron*5 + stone)
            picks[2] -= 1
            
    return answer