import re
def solution(s):
    answer = []
    s_arr = s.lstrip('{').rstrip('}').split('},{')
    s_arr.sort(key = len)
    tmp = []
    for s in s_arr:
        tmp.append(s.split(','))
        
    for t in tmp:
        for s in t:
            if int(s) not in answer:
                answer.append(int(s))
            
    return answer