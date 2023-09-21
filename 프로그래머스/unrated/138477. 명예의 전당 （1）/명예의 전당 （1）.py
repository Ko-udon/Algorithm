def solution(k, score):
    answer = []
    honer_stage = []
    for i in score:
        
        if len(honer_stage) < k:
            honer_stage.append(i)
            honer_stage.sort(reverse = True)
            answer.append(honer_stage[-1])
            continue
        
        else :
            if honer_stage[-1] < i:
                honer_stage.pop()
                honer_stage.append(i)            
            honer_stage.sort(reverse = True)
            answer.append(honer_stage[-1])
        
    
    return answer