def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1 # 편의를 위해 0원일때 값은 넣어두기
    for m in money:
        for p in range(m, n+1):
            dp[p] += dp[p - m]
    return dp[-1]%1000000007


# dp문제
# 1 ~ n원 까지 거스름돈으로 줄 수 있는 경우의 수만 필요함, 해당 경우가 뭔지는 중요하지 않음