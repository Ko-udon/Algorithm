def solution(n):
    previous = 0
    current = 1
    for i in range(2, n+1):
        previous, current = current, current + previous 
    return current % 1234567
