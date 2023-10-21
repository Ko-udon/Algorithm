def solution(num, k):
    s = list(str(num))
    return s.index(str(k)) + 1 if str(k) in s else -1