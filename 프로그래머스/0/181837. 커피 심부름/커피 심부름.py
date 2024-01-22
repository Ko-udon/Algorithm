def solution(order):
    answer = 0
    for s in order:
        if "cafelatte" in s:
            answer += 5000
        else:
            answer += 4500
    return answer