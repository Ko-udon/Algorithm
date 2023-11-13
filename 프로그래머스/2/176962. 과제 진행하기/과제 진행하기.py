def solution(plans):
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x:x[1])
    stack = []
    
    for i in range(len(plans)):
        if i == len(plans)-1:
            stack.append(plans[i])
            break
        
        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]
        if st + t <= nst: # 충분히 과제 수행이 가능함
            answer.append(sub)
            tmp_time = nst - (st+t)
            
            while tmp_time != 0 and stack: # 여분 시간이 있고 미룬 과제가 있는 경우
                tsub, tst, tt = stack.pop()
                if tmp_time >= tt: # 미룬 과제를 충분히 수행 가능한 경우
                    answer.append(tsub)
                    tmp_time -= tt
                else:
                    stack.append([tsub, tst, tt - tmp_time]) # 미룬 과제를 하다가 다시 돌아가야되는 경우
                    tmp_time = 0
            
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])
        
        
    while stack:
        s = stack.pop()
        answer.append(s[0])
        
    
    return answer