def solution(myString, pat):
    if pat not in myString:
        return 0
    answer = 0
    while pat in myString:
        i = myString.index(pat)
        myString = myString[i+1:]
        answer += 1
    return answer