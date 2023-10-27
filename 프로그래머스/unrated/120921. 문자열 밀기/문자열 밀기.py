def solution(A, B):
    tmp = A
    if A == B:
        return 0
    
    for i in range(len(A)):
        tmp = tmp[-1] + tmp[:-1]
        if tmp == B:
            return i + 1
    
    return -1