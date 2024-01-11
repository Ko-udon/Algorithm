def solution(intStrs, k, s, l):
    result = []
    for S in intStrs:
        value = int(S[s:s+l])
        if value > k:
            result.append(value)
    return result