import math
def solution(a, b):
    b = b / math.gcd(a, b)  # 약분 하기
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2