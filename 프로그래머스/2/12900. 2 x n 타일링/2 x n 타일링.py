def solution(n):
    answer = 0
    t = 1
    u = 1
    for i in range(2, n+1):
        answer = (t+u) % 1000000007
        t = u
        u = answer
    return answer