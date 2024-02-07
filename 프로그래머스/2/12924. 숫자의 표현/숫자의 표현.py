def solution(n):
    answer = 0
    v = 1
    for i in range(1, n+1):
        value = 0
        for v in range(i, n+1):
            value += v
            if value == n:
                answer += 1
            elif value > n:
                break
    return answer