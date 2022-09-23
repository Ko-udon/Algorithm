def solution(a, b):
    answer = 0
    while(a!=b):
        if(a>b):
            answer+=a
            a-=1
        elif(a<b):
            answer+=a
            a+=1
        else:
            answer=a
            return answer
    answer+=b
    return answer