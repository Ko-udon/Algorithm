def comp(answers, random):
    cnt=0
    for i in range(len(answers)):
        if answers[i]==random[i]:
            cnt+=1
    return cnt

def solution(answers):
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    n = len(answers)
    score = []
    score.append(comp(answers, arr1*(n//5)+arr1[:n%5]))
    score.append(comp(answers, arr2*(n//8)+arr2[:n%8]))
    score.append(comp(answers, arr3*(n//10)+arr3[:n%10]))

    answer=[]
    max_result = max(score)
    for i in range(3):
        if score[i]==max_result:
            answer.append(i+1)
    return answer