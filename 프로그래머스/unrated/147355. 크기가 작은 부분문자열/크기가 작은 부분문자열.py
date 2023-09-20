def solution(t, p):
    answer = 0
    size = len(p)
    first_value = p[0]
    i = 0
    while i <= len(t) - size:
        
        if t[i] > first_value:
            i+=1
            continue
        
        
        tmp = t[i:i + size]
        #print(tmp)
        if tmp <= p:
            answer+=1
        
        i+=1
        
    return answer