def solution(quiz):
    answer = []
    for s in quiz:
        i = s.index('=')
        n_value = int(s[i+1:])
        n_answer = eval(s[:i])
        if n_value == n_answer:
            answer.append('O')
        else:
            answer.append('X')
    return answer