from collections import deque

def bfs(maps, n, m):
    que = deque([(0, 0, 1)])
    visited = set()
    
    while que:
        x, y, cnt = que.popleft()
        if (x, y) in visited: continue
        visited.add((x, y))
        
        for n_x, n_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            tmp_x, tmp_y = x + n_x, y + n_y
            if 0 <= tmp_x < m and 0 <= tmp_y < n and (tmp_x, tmp_y) not in visited:
                if maps[tmp_y][tmp_x] == 1:
                    que.append((tmp_x, tmp_y, cnt + 1))
                    if tmp_x == m-1 and tmp_y == n-1:
                        return cnt + 1
    return -1
            
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(maps, n, m)