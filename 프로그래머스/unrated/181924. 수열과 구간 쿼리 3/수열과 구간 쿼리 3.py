def solution(arr, queries):
    for q in queries:
        tmp = arr[q[0]]
        arr[q[0]] = arr[q[1]]
        arr[q[1]] = tmp
    return arr