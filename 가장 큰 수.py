def solution(numbers):
    answer = sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True)
    return str(int("".join(answer)))