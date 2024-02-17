def solution(want, number, discount):
    answer = 0
    want_list = {}
    
    for i in range(len(discount)- 9):
        tmp = discount[i:i+10]
        check = 0
        for j in range(len(want)):
            if tmp.count(want[j]) != number[j]:
                check = 1
                break
                
        if check == 0:
            answer += 1

    return answer