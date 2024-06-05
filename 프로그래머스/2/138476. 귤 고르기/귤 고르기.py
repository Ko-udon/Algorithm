# def solution(k, tangerine):
#     mandarin = {}
#     for i in tangerine:
#         mandarin[i] = mandarin.get(i, 0) + 1
#     mandarin = sorted(mandarin.items(), key = lambda i : i[1], reverse = True)

#     count, mandarin_type = 0, 0
#     for value in mandarin:
#         count += value[1]
#         mandarin_type += 1
#         if count >= k:
#             return mandarin_type
#     return -1

from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counter = sorted(counter.values())
    counts = 0
    
    while counts < k:
        counts += counter.pop()
        answer += 1
    return answer