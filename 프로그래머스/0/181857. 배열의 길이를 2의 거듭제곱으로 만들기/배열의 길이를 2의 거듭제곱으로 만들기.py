def solution(arr):
    two = [1, 2, 4, 8, 16, 32, 64, 128,256, 512, 1024]
    value = 0
    for i, v in enumerate(two):
        if v >= len(arr):
            value = v
            break
    while len(arr) != value:
        arr.append(0)
    
    return arr
        