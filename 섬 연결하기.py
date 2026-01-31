import heapq

def bfs(graph, start=(0,0)):
    answer = 0
    heap = [(start)]
    visited = set()
    
    while heap:
        cost, cur = heapq.heappop(heap)
        if cur in visited: continue
        answer += cost
        visited.add(cur)
        for next_cost, next_node in graph[cur]:
            if next_node not in visited:
                heapq.heappush(heap, (next_cost, next_node))

    return answer

def solution(n, costs):
    graph = [[] for _ in range(n)]
    
    for i, j, cost in costs:
        graph[i].append((cost, j))
        graph[j].append((cost, i))
    
    return bfs(graph, (0,0))
    