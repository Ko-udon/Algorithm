def solution(n):
    answer = []
    for i in range(0, n):
        value = [0]* (n)
        value[i] = 1
        answer.append(value)
    return answer