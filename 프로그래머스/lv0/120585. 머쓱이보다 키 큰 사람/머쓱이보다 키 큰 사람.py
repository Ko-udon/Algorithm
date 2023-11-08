from bisect import bisect_left, bisect_right

def solution(array, height):
    sorted(array)
    return len(sorted(array)) - bisect_right(sorted(array), height)
