def solution(n):
    answer = []
    i=10
    while(n>0):
        answer.append(n%10)
        n=int(n/10)
    return answer