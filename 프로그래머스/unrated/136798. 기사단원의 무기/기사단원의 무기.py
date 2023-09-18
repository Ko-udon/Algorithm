def solution(number, limit, power):
    answer = 0 
    for i in range(1, number + 1): # number까지 순회
        cnt = 0 # 약수의 합을 계산하기 위한 변수
        for j in range(1, int(i ** 0.5) + 1): # 약수를 찾는 빠른 방법
            if i % j == 0:
                cnt += 1
                if i // j != j:
                    cnt += 1
            if cnt > limit:  # 제한 수치를 넘을 경우
                break
                
        if cnt > limit:  
            answer += power
        else:
            answer += cnt



    return answer