from itertools import product

def solution(numbers, target):
    tmp = ['+', '-']
    answer = 0
    for pro in product(tmp, repeat=len(numbers)):
        result = 0
        for i, n in zip(pro, numbers):
            if i == '+':
                result += n
            else:
                result -= n
        if result == target: answer += 1
    
    return answer