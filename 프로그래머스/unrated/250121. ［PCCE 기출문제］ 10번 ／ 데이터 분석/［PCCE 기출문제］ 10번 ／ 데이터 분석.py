def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for d in data:
        if ext == 'code':
            if val_ext > d[0]:
                answer.append(d)
        
        elif ext == 'date':
            if val_ext > d[1]:
                answer.append(d)
        
        elif ext == 'maximum':
            if val_ext > d[2]:
                answer.append(d)
                
        elif ext == 'remain':
            if val_ext > d[3]:
                answer.append(d)
                
    
    if sort_by == 'maximum':
        answer.sort(key = lambda x:x[2])
    
    elif sort_by == 'remain':
        answer.sort(key = lambda x:x[3])
        
    elif sort_by == 'code':
        answer.sort(key = lambda x:x[0])
        
    elif sort_by == 'date':
        answer.sort(key = lambda x:x[1])
        
    
    return answer