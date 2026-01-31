def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    answer = 1
    tmp = routes[0][1]
    for r in routes:
        if r[0] > tmp:
            answer += 1
            tmp = r[1]
    return answer