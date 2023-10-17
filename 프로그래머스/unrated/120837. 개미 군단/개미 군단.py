def solution(hp):
    answer = 0
    l = [5, 3, 1]
    for i in l:
        answer += (hp // i)
        hp = hp % i
    return answer