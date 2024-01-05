def solution(str1, str2):
    l = len(str1)
    result = ''
    for i in range(0, l):
        result = result + (str1[i] + str2[i])
    return result