def solution(numbers, direction):
    l = numbers
    return [l[-1]] + l[:-1] if direction == "right" else l[1:] + [l[0]]