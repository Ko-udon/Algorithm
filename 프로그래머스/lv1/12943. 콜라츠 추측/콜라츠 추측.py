def solution(num):
    answer = 0
    tmp=num
    if(tmp==1):
        answer=0
        return answer
    while tmp!=1:
        if(tmp%2==0):
            tmp=tmp/2
        else:
            tmp=tmp*3+1
        answer+=1
        
        if(answer>=500):
            answer=-1
            break;
        
    return answer