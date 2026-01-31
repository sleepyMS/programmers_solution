def solution(m, n, puddles):
    graph = [[0] * (m+1) for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] not in puddles and graph[i][j] == 0:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
                
    return graph[n][m] % 1000000007
    