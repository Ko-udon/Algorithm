def solution(num_list):
    answer = 0
    for n in num_list:
        value = n
        while value != 1:
            if value%2 == 0:
                value = value // 2
                answer += 1
            else:
                value = (value - 1) //2
                answer += 1
    return answer