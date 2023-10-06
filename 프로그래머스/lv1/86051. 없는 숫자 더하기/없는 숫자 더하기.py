def solution(numbers):
    return 45 - sum(list(filter(lambda x: x in numbers, range(0,10))))