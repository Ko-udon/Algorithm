def solution(s):
    answer = -1
    arr = [0, s[0]]
    for i in s[1:]:
        arr.append(i) if i!=arr[-1] else arr.pop()
    return 1 if len(arr) == 1 else 0