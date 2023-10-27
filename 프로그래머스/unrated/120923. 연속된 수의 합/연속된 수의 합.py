def solution(num, total):
    tmp = 0
    for i in range(1, num):
        tmp += i
    start = (total - tmp) // num
    return [i for i in range(start, start + num)]