def solution(strArr):
    for i, s in enumerate(strArr):
        if i%2 == 0:
            strArr[i] = s.lower()
        else:
            strArr[i] = s.upper()
    return strArr