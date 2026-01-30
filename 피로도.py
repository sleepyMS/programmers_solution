from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    for per in permutations(dungeons):
        tmp = k
        cnt = 0
        for i, j in per:
            if tmp >= i:
                tmp -= j
                cnt += 1
        answer.append(cnt)

    return max(answer)