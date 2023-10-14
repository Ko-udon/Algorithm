import math
def solution(n):
    if 7 // n > 0:
        return 1
    else:
        return math.ceil(n/7)
    