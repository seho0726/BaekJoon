from itertools import permutations

def is_prime(n):
    if n < 2 :
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    all_nums = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        
        for p in perms:
            num = int("".join(p))
            all_nums.add(num)
    
    for n in all_nums:
        if is_prime(n):
            answer += 1
        
    return answer