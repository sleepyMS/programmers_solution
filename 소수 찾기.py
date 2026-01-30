from itertools import permutations

def solution(numbers):
    set_numbers = set()
    for i in range(1, len(numbers)+1):
        tmp = list(permutations(numbers, i))
        for t in tmp:
            set_numbers.add(int("".join(t)))
    
    if not set_numbers: return 0
    max_num = max(set_numbers)
    
    is_prime = [True] * (max_num+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num ** 0.5)+1):
        for j in range(i*i, max_num + 1, i):
            is_prime[j] = False
            
    answer = 0
    for i in set_numbers:
        if is_prime[i]:
            answer += 1
    return answer