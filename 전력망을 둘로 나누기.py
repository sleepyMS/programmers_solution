def dfs(graph, n, start):
    stack = [start]
    visited = set([start])
    while stack:
        tmp = stack.pop()
        for i in graph[tmp]:
            if i not in visited:
                stack.append(i)
                visited.add(i)
    
    return abs(len(visited) - (n - len(visited)))
        
def solution(n, wires):
    answer = []
    
    for i in range(n-1):
        graph = [[] for _ in range(n+1)]
        for w in wires:
            if w == wires[i]: continue
            graph[w[0]].append(w[1])
            graph[w[1]].append(w[0])
        answer.append(dfs(graph, n, wires[i][0]))
        
    return min(answer)