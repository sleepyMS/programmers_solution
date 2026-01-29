import heapq
from collections import deque

def solution(jobs):
    n = len(jobs)
    heapq.heapify(jobs)
    que = [heapq.heappop(jobs)]
    que[0].reverse()
    heapq.heapify(que)
    
    ms = 0
    total_ms = 0
    
    while que or jobs:
        if que:
            task = heapq.heappop(que)
            if ms < task[1]:
                ms = task[1]
            ms += task[0]
            total_ms += (ms - task[1])
            print(task, ms, total_ms)
        else:
            ms += 1
        while jobs and jobs[0][0] <= ms:
            tmp = heapq.heappop(jobs)
            heapq.heappush(que, [tmp[1], tmp[0]])
    
    return total_ms // n