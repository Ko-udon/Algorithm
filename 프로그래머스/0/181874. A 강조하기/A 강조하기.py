def solution(myString):
    answer = ''
    for s in myString:
        if s == 'a':
            answer+='A'
        elif s.isupper() == True and s != 'A':
            answer+=s.lower()
        else:
            answer+=s
    return answer