from collections import deque

def dfs(graph, start):
    que = deque([start]) 
    visited = set()
    while que:
        tmp = que.popleft()

        if tmp in visited: continue
        visited.add(tmp)
        for i, c in enumerate(graph[tmp]):
            if i not in visited and c == 1:
                que.append(i)
    return visited

def solution(n, computers):
    tmp = [False] * n
    answer = 0
    while False in tmp:
        remove = dfs(computers, tmp.index(False))
        for r in remove:
            tmp[r] = True
        answer += 1
        
    return answer
            
    
        
    