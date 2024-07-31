from itertools import product

def solution(users, emoticons):
    arr = [10, 20, 30, 40]
    rates_arr = list(product(arr, repeat=len(emoticons))) # 가능한 모든 할인의 경우의 수(이모티콘의 수 만큼)
    results = []
    
    for rates in rates_arr:
        cnt, price = 0, 0

        for user in users:
            user_rate, user_price = user # 사용자별 할인율과 max금액
            cur_cnt, cur_price = 0, 0 

            for rate, emoticon_price in zip(rates, emoticons):

                if rate >= user_rate: # 할인한 이모티콘 금액 +
                    cur_price += (emoticon_price // 100 * (100 - rate))

                if cur_price >= user_price: # max금액을 넘은 경우
                    cur_cnt += 1
                    break

            if cur_cnt == 1:
                cnt += 1
            else:
                price += cur_price # 금액 누적

        results.append([cnt, price])

    return sorted(results, key=lambda x: (-x[0], -x[1]))[0]