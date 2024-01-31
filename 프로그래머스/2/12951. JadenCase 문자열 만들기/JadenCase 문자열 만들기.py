def solution(s):
    answer = ''
    arr = s.split(" ")
    for i, v in enumerate(arr):
        if v=='' or v[0].isdigit():
            arr[i] = v.lower()
        else:
            v = v.lower()
            v = v[0].upper() + v[1:]
            arr[i] = v
    answer = ' '.join(map(str, arr))
    return answer