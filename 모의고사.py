def solution(answers):
    len_a = len(answers)
    a_1 = [1,2,3,4,5]
    a_2 = [2,1,2,3,2,4,2,5]
    a_3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0] * 3
    
    for i, answer in enumerate(answers):
        if answer == a_1[i%len(a_1)]:
            result[0] += 1
        if answer == a_2[i%len(a_2)]:
            result[1] += 1
        if answer == a_3[i%len(a_3)]:
            result[2] += 1
            
    max_s = max(result)
    return [i for i, s in enumerate(result, start=1) if max_s == s]