def solution(arr, flag):
    x = []
    for i, f in enumerate(flag):
        if f:
            for j in range(0, arr[i] * 2):
                x.append(arr[i])
        else:
            x = x[:len(x) - arr[i]]
    return x