def solution(a, b):
    return sum(list(x*y for x, y in zip(a,b)))