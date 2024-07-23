def solution(money):
    n = len(money)
    dp_o = [0] * n  # 첫집 O
    dp_x = [0] * n  # 첫집 X

    dp_o[0] = money[0]
    dp_o[1] = money[0]

    dp_x[0] = 0
    dp_x[1] = money[1]

    for i in range(2, n):
        # 현재 집을 털지 않는 경우 vs 현재 집을 터는 경우
        dp_o[i] = max(dp_o[i-1], money[i] + dp_o[i-2])
        dp_x[i] = max(dp_x[i-1], money[i] + dp_x[i-2])

    # 첫집을 터는 경우, 막집은 못터니까 dp_o[n-2]까지만 가능하다
    return max(dp_o[n-2], dp_x[n-1])