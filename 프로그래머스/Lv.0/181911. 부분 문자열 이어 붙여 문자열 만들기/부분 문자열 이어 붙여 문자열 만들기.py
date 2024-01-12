def solution(my_strings, parts):
    result = ''
    tmp = 0
    for part in parts:
        s, e = part[0], part[1]
        result += my_strings[tmp][s:e+1]
        tmp+=1
    return result