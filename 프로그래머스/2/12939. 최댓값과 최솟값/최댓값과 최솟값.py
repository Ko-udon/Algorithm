def solution(s):
    answer = ''
    arr = s.split(" ")
    for i, v in enumerate(arr):
        arr[i] = int(v)
    ma = max(arr)
    mi = min(arr)
    return answer+str(mi) + " " + str(ma)