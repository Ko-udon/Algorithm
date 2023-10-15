def solution(money):
    if money < 5500:
        return [0, money]
    else:
        return [money // 5500, money % 5500]