def solution(i, j, k):
    answer = 0
    for s in range(i, j + 1):
        answer += str(s).count(str(k))
    return answer