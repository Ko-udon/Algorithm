def solution(storey):
    answer = 0
    
    while storey != 0: # 0층 까지
        n = storey % 10  # 나머지 값

        if n >= 6: # 나머지가 6 이상일 경우
            storey += 10 - n
            answer += 10 - n

        elif n == 5 and (storey // 10) % 10 >= 5: # 나머지가 5이고 그 앞에자리수도 5이상인 경우
            storey += 10 - n
            answer += 10 - n

        else: # 그 외의 경우
            answer += n
        storey = storey // 10


    return answer