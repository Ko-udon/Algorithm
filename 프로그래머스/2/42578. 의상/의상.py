# from functools import reduce

# def solution(clothes):
#     style_count = {}
#     for _, type in clothes:
#         style_count[type] = style_count.get(type, 0) + 1
    
#     return reduce(lambda x, y: x * (y + 1), style_count.values(), 1) - 1

def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
