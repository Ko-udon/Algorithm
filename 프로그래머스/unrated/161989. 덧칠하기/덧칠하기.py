def solution(n, m, section):
    answer = 0
    paint = 0
    for i in section:
        tmp = i
        if(tmp > paint):
            answer+=1
            paint = tmp + m - 1
        
    return answer