def solution(str1, str2):
    return ''.join(str1[i] + str2[i] for i in range(0, len(str1)))