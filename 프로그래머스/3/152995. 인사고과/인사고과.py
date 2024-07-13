def solution(scores):
    wh = scores[0]
    wh_sum = sum(wh)
    scores.sort(key=lambda s: (-s[0], s[1]))
    
    
    max_company, answer = 0, 1
    for s in scores:
        if wh[0] < s[0] and wh[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if wh_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer