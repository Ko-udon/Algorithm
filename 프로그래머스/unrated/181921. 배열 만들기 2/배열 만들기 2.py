def solution(l, r):
    result = []
    for i in range(l, r+1):
        if all(s in ["0", "5"] for s in str(i)):
            result.append(i)
    if len(result) == 0:
        return [-1]
            
    return result
                