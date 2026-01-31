def dp(arr):
    prev_1 = 0
    prev_2 = 0
    
    for i in arr:
        cur = max(prev_1, prev_2 + i)
        prev_2 = prev_1
        prev_1 = cur
    return prev_1

def solution(money):
    case_1 = money[:-1]
    case_2 = money[1:]
    
    return max(dp(case_1), dp(case_2))