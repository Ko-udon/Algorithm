def solution(k, ranges):
    answer = []
    arr = []
    arr.append(k)
    while k != 1:
        k = k//2 if k%2 == 0 else k*3+1
        arr.append(k)
    n = len(arr) - 1
    
    area = [0]
    for i in range(1, len(arr)):
        area.append((arr[i-1] + arr[i]) / 2)
    
    for a, b in ranges:
        if a > n+b:
            answer.append(-1)
            continue
        answer.append(sum(area[a+1:n+b+1]))
    
    return answer