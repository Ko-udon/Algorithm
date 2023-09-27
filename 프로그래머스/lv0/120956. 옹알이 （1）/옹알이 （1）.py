def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        tmp = ''
        for i in s:
            tmp += i
            if tmp in pron:
                s = s.replace(tmp,'')
                tmp = ''
                
        if tmp == '':
            answer+=1
    
    return answer