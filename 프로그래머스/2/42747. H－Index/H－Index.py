def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for i in range(len(citations)):
        if citations[i] > h:
            h = i + 1
        else:
            break
    return h

