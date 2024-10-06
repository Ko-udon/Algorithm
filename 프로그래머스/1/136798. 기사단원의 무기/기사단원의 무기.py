def solution(number, limit, power):
    answer = 0
    divisors_count = [0] * (number + 1)  # 약수의 개수를 저장할 리스트

    # 약수의 개수 계산
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors_count[j] += 1

    # 제한에 따라 결과 계산
    for cnt in divisors_count[1:]:  # 1부터 number까지의 약수 개수
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer
