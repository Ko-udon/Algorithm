from functools import reduce
def solution(box, n):
    return reduce(lambda x, y : x*y,list(i//n for i in box))
