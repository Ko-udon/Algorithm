def solution(m, n, puddles):
    answer = 0
    road = [[0 for j in range(m + 1)] for i in range(n + 1)]
    # m이 가로, n이 세로인게 핵심
    road[1][1] = 1
    
    puddles = [[j, i] for [i, j] in puddles]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                road[i][j] = 0
            else:
                road[i][j] = (road[i-1][j] + road[i][j-1]) % 1000000007


    return road[-1][-1]
    
    