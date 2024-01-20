def solution(arr):
    stk = []
    for i in range(0, len(arr)):
        if not stk:
            stk.append(arr[i])
        elif stk and stk[-1] == arr[i]:
            stk.pop()
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
    return stk if stk != [] else [-1]