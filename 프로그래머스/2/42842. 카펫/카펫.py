# def solution(brown, yellow):
#     answer = []
#     n = int(brown/2 + 2)
#     for i in range(n-3, int(n/2 - 1), -1):
#         if (i-2)*(n-i-2) == yellow:
#             return [i,n-i]


import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]