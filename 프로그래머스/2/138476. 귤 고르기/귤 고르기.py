def solution(k, tangerine):
    mandarin = {}
    for i in tangerine:
        mandarin[i] = mandarin.get(i, 0) + 1
    mandarin = sorted(mandarin.items(), key = lambda i : i[1], reverse = True)

    count, mandarin_type = 0, 0
    for key, value in mandarin:
        count += value
        mandarin_type += 1
        if count >= k:
            return mandarin_type
    return -1