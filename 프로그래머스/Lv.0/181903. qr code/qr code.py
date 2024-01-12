def solution(q, r, code):
    arr = []
    for i in range(0, len(code)):
        if i%q == r:
            arr.append(i)
    return ''.join(code[i] for i in arr)