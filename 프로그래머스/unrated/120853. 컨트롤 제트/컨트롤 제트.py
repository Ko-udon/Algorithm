def solution(s):
    answer, tmp = 0, 0
    s_arr = s.split(' ')
    for i in s_arr:
        if i != 'Z':    
            tmp = int(i)
            answer += tmp
        else:
            answer -= tmp
    return answer