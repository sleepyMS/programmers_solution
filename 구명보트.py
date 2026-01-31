def solution(people, limit):
    answer = len(people)
    people.sort()
    people_re = sorted(people, reverse=True)
    tmp = 0
    answer_tmp = 0
    for i, p in enumerate(people_re):
        if p + people[tmp] <= limit and len(people)-i-1 != tmp:
            tmp += 1
            answer_tmp += 1
            
    return answer - answer_tmp // 2
