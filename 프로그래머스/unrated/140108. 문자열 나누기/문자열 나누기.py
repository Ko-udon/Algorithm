def solution(s):
    answer = 0
    case_1=0
    case_2=0
    for i in s:
        if case_1==case_2:
            answer+=1
            a=i
        if i==a:
            case_1+=1
        else:
            case_2+=1
    return answer