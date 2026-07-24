def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs(current_word):
        
        if len(current_word) > 5:
            return
        
        if current_word:
            words.append(current_word)
        
        for v in vowels:
            dfs(current_word + v)
    
    dfs("")
    answer = words.index(word) + 1

    return answer