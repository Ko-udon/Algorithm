def solution(board, k):
    value = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+j <= k:
                value += board[i][j]
    return value