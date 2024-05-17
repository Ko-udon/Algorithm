def solution(n):
    current = 1
    previous = 0
    for i in range(1, n):
        current, previous = current + previous, current
    return current % 1234567