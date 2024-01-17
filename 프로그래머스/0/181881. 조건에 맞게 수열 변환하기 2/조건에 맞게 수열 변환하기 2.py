def solution(arr):
    before = arr.copy()
    after = arr.copy()
    n = 0
    while True:
        for i, v in enumerate(before):
            if v >= 50 and v%2==0:
                after[i] = v // 2
            elif v < 50 and v%2!=0:
                after[i] = v*2 + 1
            else:
                after[i] = v
        if before == after:
            return n
        else:
            before = after.copy()
        n+=1