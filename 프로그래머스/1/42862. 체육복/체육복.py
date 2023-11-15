def solution(n, lost, reserve):
    answer = 0
    list = []
    
    for i in range(n):
        list.append(1)
    for i in reserve:
        list[i-1] += 1
    for i in lost:
        list[i-1] -= 1

    for i in range(len(list)):
        if list[i] == 2:
            if i == 0:
                if list[1] == 0:
                    list[1] += 1
            elif i == len(list)-1:
                if list[len(list)-2] == 0:
                    list[len(list)-2] += 1
            else :
                if list[i-1] == 0:
                    list[i-1] += 1
                    list[i] -= 1
                if list[i+1] == 0 and list[i] == 2:
                    list[i+1] += 1

    for i in list:
        if i >= 1:
            answer += 1
    return answer