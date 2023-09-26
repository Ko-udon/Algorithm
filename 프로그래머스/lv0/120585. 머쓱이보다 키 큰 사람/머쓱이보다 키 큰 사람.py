from bisect import bisect_left, bisect_right

def solution(array, height):
    sorted(array)
    return len(array) - bisect_right(array, height)