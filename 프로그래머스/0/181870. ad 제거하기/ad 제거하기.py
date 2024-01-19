def solution(strArr):
    result = strArr.copy()
    for s in strArr:
        if "ad" in s:
            result.remove(s)
    return result