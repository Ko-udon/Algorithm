from collections import Counter
def solution(array):
    counter = Counter(array)
    if len(counter) == 1:
        return array[0]
    
    if counter.most_common(2)[0][1] == counter.most_common(2)[1][1] :
        return -1
    
    return counter.most_common(1)[0][0]