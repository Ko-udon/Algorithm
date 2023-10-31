def solution(sequence, k):

    dic = {idx:num for idx,num in enumerate(sequence)}
    answer = []
    start,sum = 0,0

    for idx,item in enumerate(sequence):
        end = idx
        sum += item
        while sum > k :
            sum -= dic[start]
            start += 1
        if sum == k: answer.append([start,end])
    answer.sort(key = lambda x: (x[1]-x[0],x[0]))
    return answer[0]