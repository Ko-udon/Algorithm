def solution(n):
    count_one = bin(n).count('1')
    while True:
        n = n + 1
        if bin(n).count('1') == count_one:
            break
    return n