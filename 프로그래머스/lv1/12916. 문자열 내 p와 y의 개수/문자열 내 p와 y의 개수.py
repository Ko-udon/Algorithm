def solution(s):
    answer = True
    answer=s.lower().count('p') == s.lower().count('y')
    return answer