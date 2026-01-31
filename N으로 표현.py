def solution(N, number):
    if N == number:
        return 1
    
    S = [set() for _ in range(9)]
    
    for k in range(1, 9):
        S[k].add(int(str(N) * k))
        
        for i in range(1, k):
            for a in S[i]:
                for b in S[k-i]:
                    S[k].add(a + b)
                    S[k].add(a - b)
                    S[k].add(a * b)
                    if b != 0:
                        S[k].add(a // b)
        
        if number in S[k]:
            return k
            
    return -1