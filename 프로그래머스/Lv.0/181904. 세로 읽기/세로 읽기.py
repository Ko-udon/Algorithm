def solution(my_string, m, c):
    arr = [my_string[n:n+m] for n in range(0, len(my_string), m)]
    return ''.join(s[c-1] for s in arr)
