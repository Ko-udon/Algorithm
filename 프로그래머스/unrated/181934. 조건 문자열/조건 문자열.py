def solution(ineq, eq, n, m):
    result = True
    
    if ineq == "<":
        if eq == "=":
            result = n <= m
        else:
            result = n < m
    else:
        if eq == "=":
            result = n >= m
        else:
            result = n > m
    
    return 1 if result == True else 0
        