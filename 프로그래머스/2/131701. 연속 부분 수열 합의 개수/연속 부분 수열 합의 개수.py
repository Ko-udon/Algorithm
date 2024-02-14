def solution(elements):
    answer = 0
    li = set()
    for i in range(len(elements)):
        v = elements[i]
        li.add(v)
        for j in range(i+1, i+len(elements)):
            v+=elements[j%len(elements)]
            li.add(v)
    return len(set(li))