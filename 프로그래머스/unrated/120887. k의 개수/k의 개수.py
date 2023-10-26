def solution(i, j, k):
    return sum(str(s).count(str(k)) for s in range(i, j+1))