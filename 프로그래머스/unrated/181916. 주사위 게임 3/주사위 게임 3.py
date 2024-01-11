def solution(a, b, c, d):
    result = [a, b, c, d]
    set_result = list(set(result))
    
    if len(set_result) == 4:
        return min(set_result)
    elif len(set_result) == 3:
        tmp = 0
        for i in result:
            if result.count(i) == 2:
                tmp = i
                break
        set_result.remove(tmp)
        return set_result[0]*set_result[1]
    
    elif len(set_result) == 2:
        tmp = 0
        for i in result:
            if result.count(i) >= 2:
                tmp = i
                break
        
        if result.count(tmp) == 3:
            set_result.remove(tmp)
            return (10 * tmp+set_result[0]) ** 2
        
        else :
            return (set_result[0]+set_result[1])*(abs(set_result[0] - set_result[1]))
    
    
    elif len(set_result) == 1:
        return 1111 * set_result[0]