def solution(board, skill):
    answer = 0
    tmp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    # 효율성을 위한 누적합으로 계산, 처음과 끝값만 바꾸어 누적하여 계산
    for s in skill:
        r1, c1, r2, c2, degree = s[1], s[2], s[3], s[4], s[5]
        v = -degree if s[0] == 1 else degree
        tmp[r1][c1] += v
        tmp[r2 + 1][c2 + 1] += v
        tmp[r1][c2 + 1] -= v
        tmp[r2 + 1][c1] -= v
    
    # 행 기준 누적
    for i in range(len(board)):
        for j in range(len(board[0])):
            tmp[i][j + 1] += tmp[i][j]
    
    # 열 기준 누적
    for j in range(len(board[0])):
        for i in range(len(board)):
            tmp[i + 1][j] += tmp[i][j]
    

    # 배열 연산하기
    return sum([1 for i in range(len(board)) for j in range(len(board[0])) if board[i][j] + tmp[i][j] > 0])
    
