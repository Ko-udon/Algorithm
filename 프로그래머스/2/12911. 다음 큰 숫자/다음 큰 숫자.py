def solution(n):
    count_one = bin(n).count('1') # 2진수로 변경 후 1 숫자 세기
    while True:
        n = n + 1
        if bin(n).count('1') == count_one:
            break
    return n