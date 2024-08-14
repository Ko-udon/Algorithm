# 전형적인 dp문제

def solution(n):
    dp = [0] * 16
    dp[0], dp[1] = 1, 1

    for i in range(2,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]