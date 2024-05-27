from functools import reduce

def solution(clothes):
    style_count = {}
    for _, type in clothes:
        style_count[type] = style_count.get(type, 0) + 1
    
    return reduce(lambda x, y: x * (y + 1), style_count.values(), 1) - 1