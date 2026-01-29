import heapq

def solution(operations):
    op = [o.split() for o in operations]
    deleted_min, deleted_max = [], []
    heap_min, heap_max = [], []
    
    for a, b in op:
        if a == 'I':
            heapq.heappush(heap_min, int(b))
            heapq.heappush(heap_max, -int(b))
            
        if a == 'D':
            if b == '1':
                while heap_max and -(heap_max[0]) in deleted_min:
                    tmp = -(heapq.heappop(heap_max))
                    deleted_min.remove(tmp)
                if heap_max:
                    tmp = -(heapq.heappop(heap_max))
                    deleted_max.append(tmp)
                    
            if b == '-1':
                while heap_min and heap_min[0] in deleted_max:
                    tmp = heapq.heappop(heap_min)
                    deleted_max.remove(tmp)
                if heap_min:
                    tmp = heapq.heappop(heap_min)
                    deleted_min.append(tmp)
    
    for i in deleted_max:
        heap_min.remove(i)
        
    if len(heap_min):
        return max(heap_min), min(heap_min)
    return [0, 0]