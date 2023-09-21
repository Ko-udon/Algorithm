def solution(k, score):
    answer = []
    honer_stage = []
    for i in score:     
        honer_stage.append(i)
        if len(honer_stage) > k:
            honer_stage.remove(min(honer_stage))
        answer.append(min(honer_stage))
        
    
    return answer