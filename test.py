import math

def is_prime_optimized(n):
    if n < 2: return False
    # 2부터 n의 제곱근까지만 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return False
    return True


print(is_prime_optimized(2))
