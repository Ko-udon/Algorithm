def solution(wallet, bill):
    answer = 0

    wallet.sort()
    bill.sort()

    while not check_size(wallet, bill):
        fold(bill)  # 지폐를 접기
        answer += 1  # 접은 횟수 증가

    return answer

def fold(bill):
    if bill[0] > bill[1]:
        bill[0] //= 2  # 긴 쪽을 반으로 접기
    else:
        bill[1] //= 2  # 긴 쪽을 반으로 접기

def check_size(wallet, bill):
    # 지갑과 지폐 크기 정리
    wallet.sort()
    bill.sort()

    return bill[0] <= wallet[0] and bill[1] <= wallet[1]
