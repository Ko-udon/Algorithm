def solution(clothes):
    answer = 1
    style = {}
    for c in clothes:
        style[c[1]] = style.get(c[1], 0) + 1
    
    for s in style.values():
        answer += s * answer
    return answer - 1
        