def solution(babbling):
    answer = 0
    for b in babbling:
        for pron in ['aya','ye','woo','ma']:
            if pron*2 not in b:
                b=b.replace(pron, ' ')
        if len(b.strip())==0:
            answer +=1
    return answer