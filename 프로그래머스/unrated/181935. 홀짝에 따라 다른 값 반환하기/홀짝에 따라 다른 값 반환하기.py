def solution(n):
    result = 0
    if n%2 == 0:
        l = 2
        while(l<=n):
            result += l**2
            l +=2
    else:
        l = 1
        while(l<=n):
            result += l
            l += 2
    return result
            