def solution(citations):
    citations.sort(reverse = True)
    h = 0
    
    size = len(citations)
    for i in range(size):
        if citations[i] > h:
            h = i + 1
        else:
            break
    return h

