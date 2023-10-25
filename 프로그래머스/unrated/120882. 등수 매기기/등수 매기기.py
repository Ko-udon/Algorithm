def solution(score):
    answer = []
    sum_score = list(map(lambda x : x[0] + x[1], score))
    sort_score = sorted(sum_score, key = lambda x: x / 2, reverse = True)
    
    for s in sum_score:
        answer.append(sort_score.index(s) + 1)
    
    return answer