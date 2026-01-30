from itertools import product

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    
    words = set()
    for i in range(1, len(w)+1):
        for s in product(w, repeat=i):
            words.add("".join(s))
            
    words = sorted(list(words))
    return words.index(word) + 1