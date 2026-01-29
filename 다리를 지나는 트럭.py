from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    sum_w = truck_weights[0]
    bridge = deque([[truck_weights.pop(0), 1]])
    
    while bridge:     
        if bridge[0][1] >= bridge_length:
            tmp_b = bridge.popleft()
            sum_w -= tmp_b[0]
            
        for b in bridge:
            b[1] += 1
        
        if truck_weights and sum_w + truck_weights[0] <= weight:
            tmp_w = truck_weights.pop(0)
            bridge.append([tmp_w, 1])
            sum_w += tmp_w
            
        answer += 1
    return answer