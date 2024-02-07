def solution(n):
    countOne = bin(n).count('1')
    while True:
        n = n + 1
        if bin(n).count('1') == countOne:
            break
    return n