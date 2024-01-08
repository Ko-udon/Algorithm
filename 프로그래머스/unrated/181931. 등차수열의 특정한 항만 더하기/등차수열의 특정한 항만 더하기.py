def solution(a, d, included):
    result = 0
    value = a
    for i in range(len(included)):
        if included[i] == True:
            result += value
        value += d
    return result