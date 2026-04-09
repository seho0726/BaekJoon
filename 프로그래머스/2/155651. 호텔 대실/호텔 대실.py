import heapq

def trans_time(time_str):
    h, m = map(int, time_str.split(':'))
    return 60 * h + m

def solution(book_time):
    
    # 시간 변환 -> 분으로 변환
    for a in range(len(book_time)):
        for b in range(2):
            book_time[a][b] = trans_time(book_time[a][b])
    
    book_time.sort()
    room = []
    
    for start, end in book_time:
        
        if room and room[0] <= start:
            heapq.heappop(room)
        
        heapq.heappush(room, end + 10)
    
    answer = len(room)
    return answer