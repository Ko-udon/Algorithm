def solution(n):
    if n == 1:
        return [1]
    answer = []
    for i in range(1, n+1,2):
        answer.append(i)
    
    return answer