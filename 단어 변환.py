from collections import deque

def bfs(graph, begin, target):
    que = deque([(begin, 0)])
    visited = set()
    
    while que:
        word, cnt = que.popleft()
        visited.add(word)
        
        for w in graph[word]:
            if w not in visited:
                que.append((w, cnt+1))
                if w == target:
                    return cnt+1
    return 0

def solution(begin, target, words):
    words.append(begin)
    graph = {w: [] for w in words}
    
    for k in graph.keys():
        for w in words:
            cnt = 0
            for w_c, k_c in zip(w, k):
                if w_c == k_c:
                    cnt += 1
            if cnt == len(target)-1:
                graph[k].append(w)
                
    return bfs(graph, begin, target)