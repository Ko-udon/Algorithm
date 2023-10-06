def solution(price, money, count):
    amount = sum(list(map(lambda x:x*price, range(1,count+1))))
    return amount - money if (amount - money) > 0 else 0