def solution(name):
    up_down = 0
    for c in name:
        up_down += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    n = len(name)
    min_move = n - 1
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        min_move = min(min_move, i * 2 + (n - next_i), (n - next_i) * 2 + i)
        
    return up_down + min_move