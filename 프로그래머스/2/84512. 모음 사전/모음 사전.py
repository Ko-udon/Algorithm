# def solution(word):
#     answer = 0
#     alpha  = ["A","E","I","O","U",""]
#     ans = []
#     for i in alpha:
#         for j in alpha:
#             for k in alpha:
#                 for l in alpha:
#                     for m in alpha:
#                         w = i+j+k+l+m
#                         if w not in ans: ans.append(w)
#     ans.sort()
#     answer = ans.index(word)
#     return answer

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

