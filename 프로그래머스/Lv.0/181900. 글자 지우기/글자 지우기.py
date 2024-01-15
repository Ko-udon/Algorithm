def solution(my_string, indices):
    arr = list(my_string)
    for i in indices:
        arr[i] = '*'
    answer = ''
    for s in arr:
        if s != '*':
            answer += s
    return answer
