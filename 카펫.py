def solution(brown, yellow):
    sum_cell = brown + yellow
    for i in range(3, int(sum_cell*0.5)+1):
        if sum_cell % i == 0:
            if 2*(sum_cell//i) + 2*i - 4 == brown:
                return [sum_cell//i, i]