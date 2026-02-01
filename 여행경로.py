def dfs(graph, start):
    stack = [start]
    answer = []
    
    while stack:
        top = stack[-1]
        
        if top in graph and graph[top]:
            stack.append(graph[top].pop())
        else:
            answer.append(stack.pop())
    
    return answer
    
def solution(tickets):
    country = set()
    for c in tickets:
        country.update(c)
    
    graph = {c: [] for c in country}
    
    for s, e in tickets:
        graph[s].append(e)
    for k, v in graph.items():
        graph[k] = list(sorted(v, reverse=True))
        
    return dfs(graph, "ICN")[::-1]