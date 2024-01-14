def solution(n, k):
    value = k
    num = 1
    answer = []
    while value <= n:
        answer.append(value)
        num += 1
        value = num * k
    
    return answer